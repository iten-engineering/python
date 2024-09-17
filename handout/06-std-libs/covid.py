
import json
import matplotlib.pyplot as plt
import numpy as np

filename = "handout/06-std-libs/covid.json"

with open(filename, "r") as f:
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
plt.title("Covid Switzerland")
plt.xticks(np.arange(0, len(x)+1, 80))
plt.show()

