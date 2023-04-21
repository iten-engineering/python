import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_file = "handout/08-ds-libs/number-of-earth-all.csv"
df = pd.read_csv(data_file)

df_ch = df.loc[df['Country'] == 'Switzerland']
x = df_ch.columns.values.tolist()[1:]   
y = df_ch.values.tolist()[0][1:]

plt.figure()
plt.plot(x, y)
plt.xticks(np.arange(0, len(x), 5))
plt.title("Global Footprint Switzerland")
plt.ylabel("Number of Earth")
plt.show()

