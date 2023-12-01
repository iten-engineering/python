import json
import matplotlib.pyplot as plt
import numpy as np

covid_file = "handout/06-std-libs/covid.json"

with open(covid_file) as f:
    records = json.load(f)

x = []
y = []

errors = []

for i, rec in enumerate(records):
    try:
        if rec["geoRegion"] != "CH":
            continue
        # print(rec["geoRegion"], rec["datum"], rec["entries"])
        x.append(rec["datum"])
        y.append(rec["entries"])
    except Exception as e:
        errors.append([i, str(e)] )

print("Number of records:")
print("- OK  = ", len(x))
print("- NOK = ", len(errors))

print("Errors:")
print(errors)



"""
plt.figure()
plt.plot(x,y)
plt.xticks(np.arange(0, len(x)+1, 80))
plt.show()
"""