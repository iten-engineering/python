import json
import matplotlib.pyplot as plt
import numpy as np

file = "handout/06-std-libs/covid.json"

with open(file, "r") as f:
    records = json.load(f)

x = []
y = []
for rec in records:
    if rec['geoRegion'] != "CH":
        continue
    x.append(rec['datum'])
    y.append(rec['entries'])

plt.figure()
plt.plot(x,y)
plt.xticks(np.arange(0, len(x)+1, 80))
plt.show()
