# =============================================================================
# Python examples - data science library pandas
# =============================================================================

# Pandas ist das Python Modul für Datenanalyse und Manipulation
# - Datensätze vereinen (merge)
# - Daten gruppieren (d.h. in Gruppen aufsplitten)
# - Operationen auf Gruppen ausführen
# - Label-based indexing und slicing
# - Stellt zwei Klassen zur Verfügung:
#   - 1-Dimensionale Daten (Series)
#   - 2-Dimensionale Daten mit Labels (DataFrame)

# -----------------------------------------------------------------------------
# DataFrame
# -----------------------------------------------------------------------------

# Der DataFrame ist ähnlich mit data.frame in R
# - 2-Dimensionale Daten mit Labels für Spalte/Zeile
# - Implementiert als wrapper um numpy.ndarray
#   - Operationen wie mit numpy arrays
#   - Man kann Masken brauchen (für die Indizierung)
# - Ein DataFrame wird via Klasse instanziert

import numpy as np
import pandas as pd

col_names = ["A", "B", "C"]
row_names = ["First", "Second", "Third"]
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

df = pd.DataFrame(data, row_names, col_names)
print(df)

print(df.shape)         # Tuple with number of rows and columns
print(df.shape[0])      # Number of rows
print(df.shape[1])      # Number of columns

# -----------------------------------------------------------------------------
# Slicing
# -----------------------------------------------------------------------------

print("#")
print("# Slicing I")
print("#")

# DataFrame
print(df)

# DataFrame Spalten selektieren
c1 = df["A"]
print(c1)

c2 = df.B
print(c2)

print("#")
print("# Slicing II")
print("#")

# DataFrame
print(df)

# DataFrame Zeilen selektieren
r1_r2 = df["First":"Second"]        # Beachte: Lable slincing ist inklusive End Label
print(r1_r2)

r2 = df[1:2]                        # Slicing via Index ist exklusive End Index
print(r2)

# Das loc Attribut erlaubt Label basiertes slicing von Kolonne und Zeile
# - Immer inklusiv
# - Nur Label basiert
x = df.loc["First":"Second", "B":"C"]
print(x)

# -----------------------------------------------------------------------------
# apply
# -----------------------------------------------------------------------------

# Die apply Methode erlaubt eine Funktion auf jedem Element oder series von
# einem DataFrame aufzurufen:

print("#")
print("# apply")
print("#")

sq = df.apply(np.sqrt)
print(sq)

min_per_col = df.apply(min)
print(min_per_col)


def mycalc(x):
    return 2*x
mc = df.apply(mycalc)
print(mc)

# -----------------------------------------------------------------------------
# groupby
# -----------------------------------------------------------------------------

# Mit der groupby Methode werden Daten nach einer Spalte gruppiert
# Man kann dann auf dem zurückgegebenen Objekt Funktionen pro Gruppe anwenden

print("#")
print("# groupby")
print("#")

col_names = ["A", "B"]
data = [[1, 2],
        [1, 4],
        [2, 4],
        [1, 2]]
df = pd.DataFrame(data, columns=col_names)

grouped = df.groupby("A")   # 1: 2 4 2 : mean = 8/3 = 2.67
                            # 2: 4     : mean = 4/1 = 4
print(grouped.mean())

# =============================================================================
# The end.

