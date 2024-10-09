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

Technologisch wird dazu benutzt:

* Raspberry Pi als Server
* Python, Flask, Bootstrap
* [Kanboard](https://kanboard.org/) (eine Open Source Kanban-Board Implementierung mit Rest/Python-API
* [odfdo](https://github.com/jdum/odfdo) um ein Open/Libreoffice-Document zu "patchen"


## Installation

(Ziel ist es, das alles in ein docker-compose zu packen, aber das ist noch Zukunfts-Musik)

* Initiales Herunterladen des Kanboard-Docker-Images :
* Starten des Kanboard-Images
* Anlegen eines Projektes und Export des API-Keys
* Übertragen der Daten in Umgebungs-Variablen/.env-File
* Requirements installieren
* Flask-Server starten

