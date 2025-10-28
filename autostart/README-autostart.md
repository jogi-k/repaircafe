# Autostart 


F�r autostart wurden zwei verschiedene Konzepte angewendet:

* Der Server-Part, der das Kanban-Board und die repaircafe-App starten soll, wird �ber ein script in ```/etc/init.d/``` autmatisch beim System-Start gestartet.   
    * Das script dazu befindet sich hier im Unterverzeichnis ```etc-init.d``` und heisst:
    * ```myrepairserver``` 
    * und muss entsprechend der lokalen Installation zumindest bez�glich den Aufruf-Pfaden angepasst werden.
    * Anschliessend muss es nach ```/etc/init.d/``` kopiert werden 
    * Beim Systemstart ruft es das Script ```cafestart``` hier in diesem Verzeichnis auf, welches wiederum:
        * das Kanban-Board via docker compose startet
        * die App im virtual environment startet

* Der Browser-Part, der das Dashboard f�r den Eingangs-Bereich anzeigt.
* Dieser Browser-Part wird durch den automatisch startenden/einloggenden User automatisch gestartet
* Dies wird �ber die User-Autostart-Methode im lokalen Verzeichnis ```~/.config/autostart/``` realisiert 
    * Das Startfile dazu heisst : ```repairview.desktop```
    * Auch dieses muss angepasst werden, so dass es das hier befindliche ```startbrowser``` - Script aufruft.



## Verzeichnis-Struktur 

Linke Seite:
Struktur im Repo
Rechte Seite : Beispiel auf laufendem System

```
           REPO                                 FESTPLATTE
=================================================================           
    |-- cafestart                ---->          $HOME/bin/cafestart
    |-- cafestop                 ---->          $HOME/bin/cafestop
    |-- etc-init.d                              /etc/init.d
    |   `-- myrepairserver       ---->          /etc/init.d/myrepairserver  ==> ruft cafestart und cafestop (oben) auf
    |-- README-autostart.md                     n/a
    |-- config-autostart                        $HOME/.config/autostart
    |   `-- repairview.desktop   ---->          $HOME/.config/autostart/repairview.desktop ==> ruft startbrowser (nächste Zeile) auf
    `-- startbrowser             ---->          $HOME/bin/startbrowser
```

