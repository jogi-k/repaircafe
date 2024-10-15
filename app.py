# -*- coding: utf-8 -*-
from enum import Enum
from flask import Flask, render_template, request, flash, redirect, url_for
from markupsafe import Markup
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *
from flask_bootstrap import Bootstrap5, SwitchField
import kanboard
import datetime
import base64

from pathlib import Path

from odfdo import Document

import os
from dotenv import load_dotenv

load_dotenv()


kanboard_token = os.getenv('KANBOARD_TOKEN')
kanban_board_name = os.getenv('KANBOARD_BOARD_NAME')
max_repairtime = int(os.getenv('REPARATUR_TIME'))
repair_guys = int(os.getenv('REPARATEURE'))

min_waiting_time = 5

app = Flask(__name__)
app.secret_key = 'dev'


bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


class RepairCafeForm(FlaskForm):
    first_name = StringField("Vorname")
    last_name = StringField("Nachname *", validators=[DataRequired(), Length(2, 100)])
    city = StringField("Wohnort *", validators=[DataRequired(), Length(2, 100)])
    phone = TelField("Telefon")
    email = EmailField("Email")
    turbine_mailinglist = BooleanField('Ich möchte über die nächsten Repair-Cafes in der Turbine informiert werden')
    konsumenten_mailinglist = BooleanField('Der Konsumentenschutz darf mich über Repair-Themen informieren')
    info_newspaper = BooleanField('Zeitung')
    info_poster = BooleanField('Plakataushang')
    info_social_media = BooleanField('Social Media')
    info_website = BooleanField('Newsletter/Website')
    info_mouth = BooleanField('Mund zu Mund')
    info_other = BooleanField('Anderes')
    info_other_what = StringField("")
    repair_object_type = StringField("Gegenstand *", validators=[DataRequired(), Length(2, 200)])
    repair_object_brand = StringField("Hersteller")
    repair_object_error = TextAreaField("Fehler-Beschreibung, bitte so genau wie möglich! *", validators=[DataRequired(), Length(2, 1000)])
    submit1 = SubmitField("Diesen Gegenstand registrieren")
    submit2 = SubmitField("Weitere Gegenstände registrieren")


def base64_encode_file( file_name ):

    with open(file_name, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_output = base64_encoded_data.decode('utf-8')

        return base64_output


def attach_file_to_task ( task_id, file_name ):
    kb = kanboard.Client('http://localhost/jsonrpc.php', 'jsonrpc',kanboard_token )
    project_props = kb.get_project_by_name(name=kanban_board_name)
    base64_file = base64_encode_file(file_name)
    kb.create_task_file( project_id=project_props["id"], 
                         task_id=task_id,
                         filename=file_name,
                         blob=base64_file)

def create_new_task_on_board(form):
        kb = kanboard.Client('http://localhost/jsonrpc.php', 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        task_id = kb.create_task(project_id=project_props["id"], 
                                 title=form.repair_object_brand.data + " : " + form.repair_object_type.data, 
                                 description = "# Besitzer  \n\n" + form.last_name.data + "\n# Fehler: \n\n" + form.repair_object_error.data  )
        return task_id

def get_amount_waiting_tasks( ):
        kb = kanboard.Client('http://localhost/jsonrpc.php', 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        column_props = kb.get_columns(project_id=project_props["id"])
        waiting_tasks = kb.search_tasks(project_id=project_props["id"], query="column:" + "\"" + column_props[1]["title"] + "\"" )
        return len(waiting_tasks)

def get_amount_active_tasks( ):
        kb = kanboard.Client('http://localhost/jsonrpc.php', 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        column_props = kb.get_columns(project_id=project_props["id"])
        active_tasks = kb.search_tasks(project_id=project_props["id"], query="column:" + "\"" + column_props[2]["title"] + "\"" )
        return len(active_tasks)

def get_active_time():
    kb = kanboard.Client('http://localhost/jsonrpc.php', 'jsonrpc', kanboard_token )
    project_props = kb.get_project_by_name(name=kanban_board_name)
    column_props = kb.get_columns(project_id=project_props["id"])
    active_tasks = kb.search_tasks(project_id=project_props["id"], query="column:" + "\"" + column_props[2]["title"] + "\"" )
    now = datetime.datetime.now()
    summ_in_minutes = 0 
    for active_task in active_tasks:
        starttime = datetime.datetime.fromtimestamp(active_task["date_moved"]) 
        duration = now - starttime
        summ_in_minutes = summ_in_minutes + int(duration.total_seconds()/60)
    return int(summ_in_minutes)

def get_waiting_time( ):
    waiting_tasks = get_amount_waiting_tasks()
    active_tasks = get_amount_active_tasks()
    active_tasks_active_time = get_active_time()

    if waiting_tasks + active_tasks < repair_guys :
        return min_waiting_time
    else:
        overall_waiting_time = ( waiting_tasks + active_tasks ) *  max_repairtime 
        overall_waiting_time = overall_waiting_time - active_tasks_active_time
        average_waiting_time = overall_waiting_time / int (repair_guys)
        average_waiting_time = int( int( int(average_waiting_time / 5 ) + 1) * 5)
        if average_waiting_time < min_waiting_time:
            average_waiting_time = min_waiting_time
        return average_waiting_time 
            



SOURCE = "Reparaturblatt_A4_template.odt"
TARGET = "Reparaturblatt_Okt_2024_Nr"

def save_new(document: Document, name: str):
    new_path = name
    print("Saving:", new_path)
    document.save(new_path, pretty=True)

def create_new_document( form, number ):

    document = Document(SOURCE)
    target_name = TARGET + "_" + str(number) + ".odt"
    body = document.body

    body.replace("11.11.1111", "17.10.2024")
    body.replace("2222", str(number) )
    body.replace("Hugo Egon", form.first_name.data + " " + form.last_name.data )
    body.replace("Lichtschwert", form.repair_object_type.data )
    body.replace("Force", form.repair_object_brand.data )
    body.replace("Kristall", form.repair_object_error.data)
    body.replace("hugo@egon", form.email.data)
    if form.info_newspaper.data : body.replace("□ Zeitung", "☑ Zeitung") 
    if form.info_poster.data  : body.replace("□ Plakataushang", "☑ Plakataushang")     
    if form.info_social_media.data  : body.replace("□ Internet / Soziale Medien", "☑ Internet / Soziale Medien")     
    if form.info_website.data  : body.replace("□ Newsletter", "☑ Newsletter/Website")     
    if form.turbine_mailinglist.data  : body.replace("□ Repaircafes in der Turbine", "☑ Repaircafes in der Turbine")     
    if form.konsumenten_mailinglist.data : body.replace("□ Reparaturthemen allgemein", "☑ Reparaturthemen allgemein")     
    save_new(document, target_name )
    return target_name

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/board', methods=['GET', 'POST'])
def board():
    return render_template('board.html')

@app.route('/overview', methods=['GET', 'POST'])
def overview():
    active = get_amount_active_tasks()
    waiting = get_amount_waiting_tasks()
    waiting_time = get_waiting_time ()  
    return render_template('overview.html', active=str(active), queued=str(waiting),waiting_time = str(waiting_time), repair_guys = str(repair_guys),max_repairtime = str(max_repairtime)   )

@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = RepairCafeForm()
    if form.validate_on_submit():
        flash('Reparatur regisitriert !')
        rep_nr = create_new_task_on_board(form)
        filename = create_new_document( form, rep_nr )
        attach_file_to_task( rep_nr, filename ) 
        return redirect(url_for('test_form'))
    return render_template(
        'form.html',
        form=form,
        repaircafe_form=RepairCafeForm()
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000 )
