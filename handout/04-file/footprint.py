import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "handout/04-file/number-of-earth-all.csv"

df = pd.read_csv(file)
df_ch = df.loc[df['Country'] == 'Switzerland']
print(df_ch.head(5))

print(type(df))

x = df_ch.columns.values.tolist()[1:]
y = df_ch.values.tolist()[0][1:]

plt.figure()
plt.plot(x,y)
plt.xticks(np.arange(0, len(x), 5))
plt.title("Switzerland")
plt.ylabel("Number of Earth")
plt.show()