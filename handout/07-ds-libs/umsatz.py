import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "handout/07-ds-libs/umsatz.xlsx"
df = pd.read_excel(filename)

monat = df['Monat'].tolist()
umsatz= df['Umsatz'].tolist()

xpos = np.arange(len(monat))
plt.bar(xpos, umsatz, align='center', alpha=0.5)
plt.xticks(xpos, monat)
plt.show()