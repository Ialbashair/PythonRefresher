import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data.csv')
plt.plot(data['n'], data['time'])
plt.savefig('final_plot.png')