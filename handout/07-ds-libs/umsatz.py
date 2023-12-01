import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "handout/07-ds-libs/umsatz.xlsx"

df = pd.read_excel(file)
print(df.tail())

monat = df['Monat'].tolist()
umsatz = df['Umsatz'].tolist()

xpos = np.arange(len(monat))
plt.bar(xpos, umsatz, align='center', alpha=0.5)
plt.xticks(xpos, monat)
plt.title("Umsätze 2023")
plt.ylabel("Mio CHF")
plt.xlabel("Monat")
plt.show()