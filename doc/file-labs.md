# Übungen zum Einlesen und Visualisieren von Excel, CSV und JSON Daten

## Umsatz

Laden von Excel Daten und Visualiserung als Bar Plot.

1. Schauen Sie sich die Datei `umsatz.xlsx` an. Sie hat zwei Spalten. Die erste enthält die Monate, die zweite den Umsatz des entsprechenden Monats.

2. Erstellen Sie ein Script `umsatz.py` und importieren Sie folgende Bibliotheken
   ```
   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   ```
3. Lesen sie die Excel Datei mit den Pandas Befehle pd.`read_excel(...)` in ein DataFrame mit dem Variablen Namen `df` ein und geben Sie dieses mit `print()` aus.

4. Erstellen Sie eine Liste mit den Monaten und eine Liste mit den Umsätzen mit folgenden Code:
   ```
   monat = df['Monat'].tolist()
   umsatz= df['Umsatz'].tolist()
   ```
5. Geben Sie die Monate und die Umsätze mit `print()` aus. Stimmen die Daten mit den Einträgen im Excel überein. 

6. Nun wollen wir den Barchart erstellen. Auf der X-Achse sollen die Monate erscheinen, auf der Y-Achse die Umsätze. Fügen Sie folgenden Code ein:
   ```
   xpos = np.arange(len(monat))
   plt.bar(xpos, umsatz, align='center', alpha=0.5)
   
   plt.show()
   ```
7. Führen Sie den Code aus. Die Monate sind noch nicht
mit den Namen beschriftet, sondern nur mit der Nummer. 
Ergänzen sie den Code nach `plt.bar()` wie folgt und führen Sie den Code anschliessend nochmals aus.
   ```
   plt.xticks(xpos, monat)
   ```
8. Fügen Sie der Grafik einen Titel bei und beschriften Sie die X- und Y-Achse. Benutzen Sie dazu die Befehle `plt.title()`, `plt.xlabel()` und `plt.ylabel()`. 

9. Führen Sie das Programm nochmals aus und überprüfen Sie Ihr Resultat.

## Global Footprint

Laden und Filtern von CSV Daten und Visualisiern als Line Chart mit Hilfe eines Notebooks.

1. Schauen Sie sich die Datei `number-of-earth-all.csv` an. Die erste Spalte enthält die Länder, anschliessend folgt die Kennzahl **Number of Earth** pro Jahr ab 1961.

2. Erstellen Sie das Jupiter Nootebook `footprint.ipynb` und importieren Sie folgende Bibliotheken
   ```
   %matplotlib inline

   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   ```
   Mit der Angabe `%matplotlib inline` werden die Matplotlib Grafiken in das Notebook eingebettet.

3. Lesen sie die CSV Datei mit den Pandas Befehle pd.`read_csv(...)` in ein DataFrame mit dem Variablen Namen `df` ein und geben Sie die ersten 5 Zeilen mit `print(df.head(5))` aus.

4. Filtern Sie die Daten für die Schweiz mit dem folgenden Befehl und geben Sie die Daten aus:
   ```
   df_ch = df.loc[df['Country'] == 'Switzerland']
   print(df_ch.head(5))
   ```

5. Als X-Achse sollen wie Jahre dargestellt werden. Filtern sie diese wie folgt:
   ```
    x = df_ch.columns.values.tolist()[1:]
    print("x:", x)
   ```

6. Als Y Werte werden folgende Daten selektiert:
   ```
   y = df_ch.values.tolist()[0][1:]
   print("y:", y)
   ```

7. Plotten Sie den Line Chart mit folgendem Commands:
   ```
   plt.figure()
   plt.plot(x,y)
   plt.show()
   ```

8. Erstellen Sie einen Titel und beschriften Sie die Y-Achse. 

9. Die X-Achse ist noch nicht ideal beschriftet. Fügen Sie folgenden Code vor dem `plt.show()` Befehl ein:
   ```
   plt.xticks(np.arange(0, len(x), 5))
   ```

10. Führen Sie das Programm nochmals aus und überprüfen Sie Ihr Resultat.

## Covid CH

Laden von JSON Daten, Filter der Covid Zahlen für die gesammte Schweiz und Visualiserung als Line Chart.

1. Schauen Sie sich die Datei `COVID19Cases_geoRegion.json` im VS Code an. Uns interessieren die drei folgenden Felder:
- geoRegion
- datum
- entries


Sie hat zwei Spalten. Die erste enthält die Monate, die zweite den Umsatz des entsprechenden Monats.

2. Erstellen Sie ein Script `covid.py` und importieren Sie folgende Bibliotheken
   ```
   import json
   import matplotlib.pyplot as plt
   import numpy as np
   import pandas as pd
   ```
3. Lesen sie die JSON Datei mit den Befehle `json.load(...)` innerhalb eines `with` Blocks in die Variable `records` ein.

4. Erstellen Sie zwei leere listen für die X- und Y-Achsenwerte.

5. Iterieren Sie über alle Records und filtern Sie die  Werte aus der `geoRegion` "CH". Das Feld `datum` wird zur Liste für die X-Achse hinzugefügt. Das Feld `entries` kommt in die Liste für die Y-Achse.

6. Erstellen Sie einen plot mit der Matplotlib. Die X-Achse können sie mit folgendem Befehl optimieren:
   ```
   plt.xticks(np.arange(0, len(x)+1, 80))
   ```

7. Speichern Sie die Grafik als PNG Datei.

8. Führen Sie das Programm nochmals aus und überprüfen Sie Ihr Resultat.
