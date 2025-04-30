import json
import matplotlib.pyplot as plt
import numpy as np

filename = "handout/06-std-libs/covid.json"

with open(filename, "r") as f:
    records = json.load(f)

x = []
y = []

for rec in records:
    if rec["geoRegion"] != "CH":
        continue
    # print(rec["geoRegion"], rec["datum"], rec["entries"])
    x.append(rec["datum"])
    y.append(rec["entries"])

# print("x:",x)
# print("y:",y)

plt.figure()
plt.plot(x,y)
plt.xticks(np.arange(0, len(x)+1, 80))
plt.title("Covid Schweiz")
plt.ylabel("Gemeldete Fälle")
plt.show()




