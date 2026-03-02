# Simple test of the used library: Fill PDF, Reparaturblatt with Demo-Data

import pymupdf

doc = pymupdf.open("Reparaturblatt_A4_template_form.pdf")
for page in doc: 
    widgets = page.widgets()
    for widget in widgets:
        if widget.field_name == "Beschreibung_Defekt": 
            widget.field_value = "Kristall hat nicht genug Leistung"
            widget.update()
        if widget.field_name == "Datum_1": 
            widget.field_value = "07.03.2026"
            widget.update()
        if widget.field_name == "Datum_2": 
            widget.field_value = "07.03.2026"
            widget.update()
        if widget.field_name == "Gegenstand": 
            widget.field_value = "Laserschwert"
            widget.update()
        if widget.field_name == "Marke": 
            widget.field_value = "UseTheForce"
            widget.update()
        if widget.field_name == "Name": 
            widget.field_value = "Luke Skywalker"
            widget.update()
        if widget.field_name == "Number": 
            widget.field_value = "007"
            widget.update()
        if widget.field_name == "Reparierender": 
            widget.field_value = "Obi Wan Kenobi"
            widget.update()
        if widget.field_name == "emailadress": 
            widget.field_value = "luke@skywalker.tatooine"
            widget.update()
        if widget.field_name == "check_newsletter": 
            widget.field_value = True
            widget.update()
        if widget.field_name == "check_plakat": 
            widget.field_value = True
            widget.update()
        if widget.field_name == "check_socialmedia": 
            widget.field_value = True
            widget.update()
        if widget.field_name == "check_zeitung": 
            widget.field_value = True
            widget.update()
        if widget.field_name == "info_konsumentenschutz": 
            widget.field_value = True
            widget.update()
        if widget.field_name == "info_repaircafe": 
            widget.field_value = True
            widget.update()
doc.save("filled_flattened.pdf", deflate=True)
