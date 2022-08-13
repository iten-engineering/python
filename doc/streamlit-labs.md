# Streamlit

## Hello World

### Overview

Kennenlernen des streamlit Framework.

![Hello Streamlit](../../img/hello-streamlit.png)

### Tasks

1. Gehen sie auf die Web Site https://streamlit.io/ und erkunden sie die Dokumentation.

2. Erstellen Sie eine Datei hello-streamlit.py und implementieren Sie die Hello World Anwendung gemäss der Einführung. 

3. Starten Sie die Anwendung mit dem folgendem Befehl in einem Terminal:
   ```
    streamlit run hello-streamlit.py 
   ```

4. Nach einem erfolgreichen Start wird eine URL angezeigt. Öffnen Sie einen Browser und schauen Sie sich die Anwendung an.

5. Ändern Sie etwas im Test und drücken sie den Refresh Button im Browser. Die Anpassung sollte jetzt ersichtlich sein.

## Sales

### Overview
Einlesen einer Excel Datei mit Verkaufszahlen pro Stadt, Anzeige als Tabelle und Balkendiagramm via Web Anwendung. 

![Sales](../../img/sales.png)

### Tasks

1. Öffnen Sie die Datei `sales.xlsx` und schauen Sie sich die Daten an.

2. Importieren sie folgende Bibliotheken:
   ```
   import pandas as pd
   import streamlit as st
   ```

3. Laden Sie die Excel Datei in eine DataFrame variable `df`.

4. Setzen Sie den Monat als Index Spalte mit dem Befehl:
   ```
   df = df.set_index('Monat', drop=True)
   ```

5. Definieren Sie mit Streamlit einen Titel und laden Sie unterhalb vom Titel das Logo `sales.png`.
   Starten Sie die Anwendung und schauen Sie ob Titel und Logo angezeigt werden.

6. Erstellen Sie mit Streamlit einen Untertitel **Raw data** und zeigen Sie die Daten mit den Streamlit Befehl
   `st.dataframe(df)` an.
   Starten Sie die Anwendung und prüfen Sie das Resultat.

7. Bauen Sie eine Checkbox ein mit den Namen **Show** und zeigen Sie die Tabelle mit dem DataFrame nur an,
   wenn die Checkbox angewählt ist.
   Starten Sie die Anwendung und prüfen Sie das Resultat.
  ![Show](../../img/sales-show-table.png)

8. Erstellen Sie mit Streamlit einen Untertitel **Chart** und zeigen Sie die Daten mit den Streamlit Befehl
   `st.bar_chart(df)` an.
   Starten Sie die Anwendung und prüfen Sie das Resultat.

9. Fügen sie eine SelectBox ein mit der die einzelnen Städte oder alle zusammen angewählt werden können.
![SelectBox](../../img/sales-select-town.png)

10. Passen Sie die Anzeige vom Chart so an, dass entweder die Daten einer einzelnen Stadt oder alle angezeigt werden, so wie Sie es in der SelectBox angewählt haben.
Starten Sie die Anwendung und prüfen Sie das Resultat.
![Sales Bern](../../img/sales-bern.png)

11. Fügen Sie im der Excel Datei eine neue Stadt hinzu und passen Sie den Code so an, das die Auswahl der    SelectBox automatisch anhand der Excel Daten generiert wird.
    Starten Sie die Anwendung und prüfen Sie das Resultat.

12. Fügen sie am Ende der Anwendung eine Trennlinie ein und darunter einen Copyright Eintrag mit Ihrem Firmennamen.
