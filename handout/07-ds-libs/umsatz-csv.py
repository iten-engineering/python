
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file = "handout/07-ds-libs/umsatz.csv"

df = pd.read_csv(file)

monat = []
for m in df.columns.to_list():
    monat.append(m.strip().strip("'"))

umsatz= df.values[0]

plt.bar(monat, umsatz, align='center', alpha=0.5)
plt.show()
exit()
