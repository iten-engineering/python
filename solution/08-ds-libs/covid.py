import json
import matplotlib.pyplot as plt
import numpy as np

file = "solution/08-ds-libs/covid.json"

with open(file) as f:
    records = json.load(f)

x = []
y = []

for rec in records:
    # skip other regions
    if rec['geoRegion'] != "CH":
        continue
    # continue processing
    x.append(rec['datum'])
    y.append(rec['entries'])

plt.figure()
plt.plot(x,y)
plt.xticks(np.arange(0, len(x)+1,100))
plt.show()



