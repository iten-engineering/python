
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "handout/07-ds-libs/umsatz.xlsx"

df = pd.read_excel(file)

monat = df['Monat'].tolist()
umsatz= df['Umsatz'].tolist()

plt.bar(monat, umsatz, align='center', alpha=0.5)
plt.show()
exit()
