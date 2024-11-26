import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

filename = "handout/07-ds-libs/umsatz.xlsx"

df = pd.read_excel(filename)

monat = df['Monat'].to_list()
umsatz= df['Umsatz'].to_list()


plt.figure()

plt.title("Umsatzprognose 2024")
plt.ylabel("Umsatz in Mio CHF")

plt.bar(monat, umsatz, align='center', alpha=0.5)
plt.show()
