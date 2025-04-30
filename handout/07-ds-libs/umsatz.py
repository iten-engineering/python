import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "handout/07-ds-libs/umsatz.xlsx"
df = pd.read_excel(filename)

monat = df['Monat'].tolist()
umsatz = df['Umsatz'].tolist()

plt.figure()
plt.bar(monat, umsatz)
plt.title("Umsätze 2024")
plt.ylabel("in Tsd. CHF")
plt.show()
