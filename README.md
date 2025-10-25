# repaircafe

Hilfstool f�r unser [Repaircafe](https://www.turbine-brunnen.ch/repaircafe/) (Registrierung, Doc-Creation, Taskboard, �bersicht, Wartezeit)

Dies ist eine Sammlung um eine webbasierte Hilfe f�r unser Repaircafe anzubieten.  
Das Tool l�uft auf einem Raspberry-Pi als Server und bietet folgende Dinge an:

* Webbasierte Registrierung von Kunden und Reparatur-Gegenst�nden
* �bertragung der Daten in ein Libreoffice-Document, das wird automatisch durch den Server ausgedruckt
( wir sind noch nicht ganz fertig mit der Digitalisierung ...)
* �betragung der Daten in ein Kanban-Board um die Warteschlange, die Reparaturen und den Fortschritt zu visiualisieren
* �bertragung der Daten in eine Datenbank um sie weiter auszuwerten und gesammelt an den Konsumentenschutz zu �bertragen (noch nicht, derzeit ist das Kanban-Board die Datenbank...
* Auswertung der Daten und Anzeige in einer �bersicht
* mehr sp�ter, Ideen gibt es noch genug...

## Schema 

![Schema-Repaircafe](pics/Repaircafe.drawio.svg)


## Begr�ssungs-Dashboard

Mit diesem Dashboard im Eingangsbereich werden die potentiellen Kunden "begr�sst", so dass sie schon absch�tzen k�nnen, wie lange sie nach der Registrierung warten m�ssen, bzw. Kaffee und Kuchen geniessen d�rfen

![Eingangs-Dashboard](pics/dashboard.png)


## Registrierungs-Form

Wenn sie die gesch�tzte Wartezeit nicht abschreckt, k�nnen sie sich dann selbst an einem unserer (bis zu 4, je nach Andrang...) Registrierungs-Laptops registrieren.
Nat�rlich helfen wir bei diesem Schritt auch weiterhin mit mehreren Helfern im Eingangsbereich.   
Wir haben doch oft auch �ltere Kunden und Kundinnen.


![Registrier-Formular](pics/registrier_formular.png)


## Unser Formular 

Beim Abschicken des Formulars wird das Dokument automatisch ausgedruckt und es landet als "Story" in unserem Kanban-Board. Die G�ste m�ssen dann noch beim "Empfang" vorbei, dort unterschreiben sie die Haftungs-Begrenzung und bekommen einen Pager mit Ihrer Nummer. 

So sieht das Formular dann aus dem Drucker aus:


![Reparatur-Blatt zum Unterschreiben](pics/dokument_sm.png)

## Unser Kanban-Board

Das Kanban-Board wird (noch) vom Empfang gesteuert. Bei der Selbst-Registrierung durch die G�ste landen die neu registrierten Gegenst�nde in der Spalte **Neu/Kein Kunde** und erst nach der Unterschrift zur Haftungs-Begrenzung und der Ausgabe des Pagers wird die Karte in die Spalte **Wartend** verschoben.  
Ab diesem Moment wird die Karte/der Gegenstand dann auch mit in die Berechnung der Wartezeit auf dem Dashboard einbezogen.

Das gleiche Kanbanboard wird in den Reparier-R�umlichkeiten dann auch per Beamer oder zus�tzlichen Monitoren den Reparateuren gezeigt, so dass diese wiederum sehen k�nnen:

* Wie gross die Schlange am Empfang / im Cafe ist.
* Was als n�chstes in "der Queue" ist und vielleicht schon bestimmtes Know-How, das sie haben, nach vorne melden k�nnen.



![Kanban-Board](pics/kanbanboard.png)


# Stack

Technologisch wird dazu benutzt:

* Raspberry Pi als Server
* Python, Flask, Bootstrap
* [bootstrap-flask](https://github.com/helloflask/bootstrap-flask) Eine Kombination mit templates , Nachfolger von flask-bootstrap. Die Demo-App wurde als Basis verwendet.
* [Kanboard](https://kanboard.org/) (eine Open Source Kanban-Board Implementierung mit Rest/Python-API
* [odfdo](https://github.com/jdum/odfdo) um ein Open/Libreoffice-Document zu "patchen"


# Installation

(Ziel ist es, das alles in ein docker-compose zu packen, momentan ist das nur f�r das Kanban-Board der Fall, das Python-Programm muss noch von Hand installiert werden) 

* Starten des Kanbanboards : docker-compose / docker compose im Unterverzeichnis kanboard ```docker compose -f kanboard/docker-compose.yml up -d```
* Anlegen eines Projektes und Export des API-Keys
    * Dazu einmal auf dem Raspi (oder localhost) die URL : ```http://localhost:8880/settings/api``` ansteuern
    * Den API-Key notieren
    * ![Api-Key](pics/api_key.png)
    * Ein Projekt Anlegen : ```http://localhost:8880/project/create```
    * Den Projekt-Namen notieren
    * ![ProjectName](pics/project_name.png) 
* �bertragen der Daten in Umgebungs-Variablen/.env-File, siehe env-template , bitte kopieren nach .env und mit den ermittelten Werten bef�llen 
* Virtual environment anlegen : ``` python -m venv venv``` (einmalig)
* Virtual environment aktivieren : ```source venv/bin/activate```
* Requirements installieren:  ```pip install -r requirements.txt``` (einmalig)
* Flask-Server starten : ```python app.py```
* Browser starten, folgende Routes werden darzeit unterst�tztz:
    * ```localhost:8880``` :  Kanban-Board
    * ```localhost``` : Eingabe-Formular f�r die Selbstregistrierung
    * ```localhost/overview``` : das �bersichts-Dashboard f�r den Empfang
    * ```localhost/config``` : Konfiguration der angestrebten Reparatur-Dauer und der Anzahl Reparierenden  
    * ```localhost/board ``` : Nochmal das Kanbanboard, einfacher zu merken ...  
    * ```localhost/publicboard ``` : Nochmal das Kanbanboard, allerdings read only ...  
    * ```localhost/toggle      ``` : Ein alternierendes Board zwischen Dashboard und read-only Kanban, f�r die Reparierenden ...  


# Autostart

Die Installation geht davon aus, dass der Raspberry Pi Server f�r mehrere Dinge gleichzeitig zust�ndig ist 

* Bereitstellng des Kanban-Boards
* Bereitstellung der repaircafe Web-App mit Formular, �bersicht, Fernsteuerung des Kanban-Boards etc
* Anzeige des �bersichts-Dashboards an einem angeschlossenen Monitor

Dazu gibt es ein paar autostart-Helper im Unterverzeichnis ```autostart``` ,  dort befindet sich eine [Readme-Datei](autostart/README-autostart.md)

 


# Ideen / Link-Sammlung / Tipps

## Andere Kanban-Boards

* Basic: https://github.com/ritakurban/Kanban-Board
* Basic: https://github.com/kevinyang372/kanban_board
* Extended, Trello-artig : https://github.com/FLiotta/Tiquet : Outdated, 6 years old
* Extended: kan.bn , Trello- Artig : https://github.com/kanbn/kan , sieht gut aus, aber leider keine Nummern out of the Box.
* Extended: kaneo , Trello-Artig : https://github.com/usekaneo/kaneo , sieht noch besser aus, aber weder mit lite noch mit standard-config schnell zum Laufen gebracht..
* Extended: wekan, https://github.com/wekan/wekan/tree/main, versucht via snap, hat nicht funktioniert, konnte mich nicht einloggen.



## Erweiterung der Anzeige auf Divoom-Pixoo

* https://github.com/roemer/govoom
* https://doc.divoom-gz.com/web/#/12?page_id=219
* https://github.com/Roemer/govoom/wiki/Get-data-from-Home-Assistant
* https://pypi.org/project/pixoo/
* https://github.com/SomethingWithComputers/pixoo

## Tipps 

* Two Forms/ Two Buttons : https://stackoverflow.com/questions/39738069/flask-bootstrap-with-two-forms-in-one-page
* Configuration of Kanboard : https://github.com/kanboard/kanboard/issues/4894
* base64-encode a file : https://gist.github.com/juliensalinas/15789d241f28b1ce45f0c22e11ba894a
* Allow binding on port 80 for normal user : e.g. https://superuser.com/a/1482188



### Die Spalten heissen:
 
* Neu / Kein Kunde
* Warteschlange
* In Arbeit
* Erledigt

(Sollte mal noch per Script automatisiert werden...)


