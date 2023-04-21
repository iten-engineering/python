import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file = "handout/08-ds-libs/umsatz.xlsx"
df = pd.read_excel(data_file)
print(df.head(3))

monat = df['Monat'].tolist()
umsatz= df['Umsatz'].tolist()

xpos = np.arange(len(monat))
plt.bar(xpos, umsatz)
plt.xticks(xpos, monat)
plt.title("Umsätze Jan - Dez")
plt.xlabel("Monat")
plt.ylabel("Umsatz")
plt.show()


