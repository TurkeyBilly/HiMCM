import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

data = pd.read_csv('Month.csv')
water = pd.read_csv('HL.csv')

output = "water.png"
fig, ((ax1, ax2, ax3)) = plt.subplots(3,1)
fig.set_size_inches(10, 15)

ax1.plot((data['y']+23220)/12, data['wl'], color='orange', label='Water Level by Month')
ax1.legend(loc='best')
ax2.plot(water['y'], water['l'], color='blue', label='Low Water Level by Year')
ax2.plot(water['y'], water['h'], color='red', label='High Water Level by Year')
ax2.plot(water['y'], (water['l']+water['h'])/2, color='purple', linestyle='dotted', label='Average Water Level by Year')
ax2.legend(loc='best')

ax3.plot((data['y']+23220)/12, data['wl'], color='orange', linestyle='dotted', label='Water Level by Month')
ax3.plot((data['y']+23220)/12, data['ra6'], color='purple', label='Rolling Average (6 months)')
ax3.plot((data['y']+23220)/12, data['ra12'], color='blue', label='Rolling Average (12 months)')
ax3.legend(loc='best')

ax1.grid(True)
ax2.grid(True)
ax3.grid(True)

ax1.set_title('Monthly Water Level Since 1935')
ax2.set_title('Annual High, Low, and Average Water Levels Since 1935')
ax3.set_title('Monthly Water Levels with Rolling Averages Since 1935')

plt.savefig(output)
print("Graph exported to", output)
