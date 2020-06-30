import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/john/python-dashboards/first-dashboard-starworks/data/ouraRingBrokenDates.csv')
df.set_index('date')

df.head()

print(df.columns)
print(df['Sleep Score'].values)
print(df)

df.plot(kind='line',x='date',y='Total Sleep Time')
plt.show()
