# Autostart 


Für autostart wurden zwei verschiedene Konzepte angewendet:

* Der Server-Part, der das Kanban-Board und die repaircafe-App starten soll, wird über ein script in ```/etc/init.d/``` autmatisch beim System-Start gestartet.
     * Das script dazu befindet sich hier im Unterverzeichnis ```etc-init.d``` und heisst:
     * ```myrepairserver``` 
     * und muss entsprechend der lokalen Installation zumindest bezüglich den Aufruf-Pfaden angepasst werden.
     * Anschliessend muss es nach ```/etc/init.d/``` kopiert werden 
     * Beim Systemstart ruft es das Script ```cafestart``` hier in diesem Verzeichnis auf, welches wiederum:
           * das Kanban-Board via docker compose startet
           * die App im virtual environment startet

* Der Browser-Part, der das Dashboard für den Eingangs-Bereich anzeigt.
* Dieser Browser-Part wird durch den automatisch startenden/einloggenden User automatisch gestartet
* Dies wird über die User-Autostart-Methode im lokalen Verzeichnis ```~/.config/autostart/``` realisiert 
    * Das Startfile dazu heisst : ```repairview.desktop```
    * Auch dieses muss angepasst werden, so dass es das hier befindliche ```startbowser``` - Script aufruft.



## Verzeichnis-Struktur 

```
    |-- cafestart
    |-- cafestop
    |-- config-autostart
    |   `-- repairview.desktop
    |-- etc-init.d
    |   `-- myrepairserver
    |-- README-autostart.md
    `-- startbrowser
```

