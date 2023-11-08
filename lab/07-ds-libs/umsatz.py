import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "handout/05-file/umsatz.xlsx"
df = pd.read_excel(filename)

print(df.head(3))

monat = df['Monat'].tolist()
umsatz= df['Umsatz'].tolist()

xpos = np.arange(len(monat))
plt.bar(xpos, umsatz, align='center', alpha=0.5)
plt.xticks(xpos, monat)

plt.title("Umsätze 2022")
plt.xlabel("Monate")
plt.ylabel("Umsatz in 1000 CHF")

plt.show()


