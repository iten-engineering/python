import json
import matplotlib.pyplot as plt
import numpy as np


filename = "handout/06-std-libs/covid.json"
with open(filename, "r") as f:
    records = json.load(f)

x = []
y = []
for record in records:
    if record['geoRegion'] != "CH":
        continue
    x.append(record['datum'])
    y.append(record['entries'])


plt.figure()
plt.xticks(np.arange(0, len(x)+1, 80))
plt.plot(x,y)
plt.title("Covid Schweiz")
plt.ylabel("Anzahl registrierte Fälle")
# plt.savefig("covid.png")
plt.show()