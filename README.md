# repaircafe

Hilfstool für unser Repaircafe (Registrierung, Doc-Creation, Taskboard, Übersicht, Wartezeit)

Dies ist eine Sammlung um eine Webbasierte Hilfe für unser Repaircafe anzubieten.  
Das Tool läuft auf einem Raspberry-Pi als Server und bietet folgende Dinge an:

* Webbasierte Registrierung von Kunden und Reparatur-Gegenständen
* Übertragung der Daten in ein Libreoffice-Document um direkt ausgedruckt und unterschrieben zu werden
( wir sind noch nicht ganz fertig mit der Digitalisierung ...)
* Übetragung der Daten in ein Kanban-Board um die Warteschlange, die Reparaturen und den Fortschritt zu visiualisieren
* Übertragung der Daten in eine Datenbank um sie weiter auszuwerten und gesammelt an den Konsumentenschutz zu übertragen
* Auswertung der Daten und Anzeige in einer Übersicht
* mehr später, Ideen gibt es noch genug...

## Stack

Technologisch wird dazu benutzt:

* Raspberry Pi als Server
* Python, Flask, Bootstrap
* [bootstrap-flask](https://github.com/helloflask/bootstrap-flask) Eine Kombination mit templates , Nachfolger von flask-bootstrap. Die Demo-App wurde als Basis verwendet.
* [Kanboard](https://kanboard.org/) (eine Open Source Kanban-Board Implementierung mit Rest/Python-API
* [odfdo](https://github.com/jdum/odfdo) um ein Open/Libreoffice-Document zu "patchen"


## Installation

(Ziel ist es, das alles in ein docker-compose zu packen, aber das ist noch Zukunfts-Musik)

* Initiales Herunterladen und Starten des Kanboard-Docker-Images : ```docker run -d --name kanboard -p 80:80 -t kanboard/kanboard:v1.4.0```
* (Späteres Starten des Kanboard-Images : ```docker start kanboard```
* Anlegen eines Projektes und Export des API-Keys
* Übertragen der Daten in Umgebungs-Variablen/.env-File, siehe env-template , bitte befüllen und nach .env umbenennen
* Requirements installieren:  ```pip install -r requirements.txt```
* Flask-Server starten : ```python app.py```
* Browser auf localhost:80 (Kanban-Board) und auf localhost:5000 (Formular, Übersicht) starten.


## Ideen / Link-Sammlung / Tipps

### Andere Kanban-Boards

* Basic: https://github.com/ritakurban/Kanban-Board
* Basic: https://github.com/kevinyang372/kanban_board
* Extendend, Trello-artig : https://github.com/FLiotta/Tiquet

### Erweiterung der Anzeige auf Divoom-Pixoo

* https://github.com/roemer/govoom
* https://doc.divoom-gz.com/web/#/12?page_id=219
* https://github.com/Roemer/govoom/wiki/Get-data-from-Home-Assistant
* https://pypi.org/project/pixoo/
* https://github.com/SomethingWithComputers/pixoo

### Tipps 

https://stackoverflow.com/questions/39738069/flask-bootstrap-with-two-forms-in-one-page


### Die Spalten heissen:
 
* Neu / Kein Kunde
* Warteschlange
* In Arbeit
* Erledigt

(Sollte mal noch per Script automatisiert werden...)

