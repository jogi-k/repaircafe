# Just a collection of simple functions for manual playing around with
# the api to kanboard. Not used itself in the project, apart from being the origine for
# some of the main working functionality of the app

# -*- coding: utf-8 -*-
from enum import Enum
import kanboard
import datetime

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()


kanboard_token = os.getenv('KANBOARD_TOKEN')
kanban_board_name = os.getenv('KANBOARD_BOARD_NAME')
kanban_board_api_point = os.getenv('KANBOARD_ENDPOINT')


def fetch_meta_data_from_task ( task_id):
        kb = kanboard.Client(kanban_board_api_point, 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        meta_data = kb.get_task_metadata( task_id = task_id )
        print ( meta_data)


def create_new_task_on_board():
        kb = kanboard.Client('kanban_board_api_point', 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        task_id = kb.create_task(project_id=project_props["id"], 
                                 title="Hugo", 
                                 description = "# Besitzer  \n\n Egon" )
        params =  { "metaname1" : "metadata1" ,  "metaname2" : "metadata2" } 
        kb.save_task_metadata(task_id=task_id , values = params);
        return task_id

def get_amount_waiting_tasks( ):
        kb = kanboard.Client('kanban_board_api_point', 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        column_props = kb.get_columns(project_id=project_props["id"])
        waiting_tasks = kb.search_tasks(project_id=project_props["id"], query="column:" + "\"" + column_props[1]["title"] + "\"" )
        return len(waiting_tasks)

def get_amount_active_tasks( ):
        kb = kanboard.Client('kanban_board_api_point', 'jsonrpc',kanboard_token )
        project_props = kb.get_project_by_name(name=kanban_board_name)
        column_props = kb.get_columns(project_id=project_props["id"])
        active_tasks = kb.search_tasks(project_id=project_props["id"], query="column:" + "\"" + column_props[2]["title"] + "\"" )
        return len(active_tasks)

def get_active_time():
    kb = kanboard.Client('kanban_board_api_point', 'jsonrpc', kanboard_token )
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
            


if __name__ == '__main__':
#    my_task_id = create_new_task_on_board( )
#    print("Task-ID = " + str(my_task_id) )
    fetch_meta_data_from_task( 32 )
