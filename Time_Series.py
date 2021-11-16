from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print('Initializing...')
ex1 = pd.read_excel(r'C:\Users\14809\Desktop\copy\LowHigh.xlsx')
ex2 = pd.read_excel(r'C:\Users\14809\Desktop\copy\MonthlyElevation.xlsx')


month2 = [col for col in ex2 if not col.startswith('Unnamed:')]
del month2[0]

yr2 = [int(ex2.iat[i, 0]) for i in range(ex2.shape[0]-1)]

accurate_x = []
x = []
y = []

for m in range(0, ex2.shape[0]-1):
    l = 0
    for num in range(1, 13):
        l += 1
        # It's very important to remove the string, isnan(str) yield error
        if np.isnan(ex2.iat[m, num]):
            continue
        accurate_x.append([ex2.iat[m, 0], l])
        x.append(ex2.iat[m, 0]+(l-1)/12)
        y.append(ex2.iat[m, num])
assert(len(x)==len(y))


month = dict(
    Jan=1,
    Feb=2,
    Mar=3,
    Apr=4,
    May=5,
    Jun=6,
    Jal=7,
    Aug=8,
    Sep=9,
    Oct=10,
    Nov=11,
    Dec=12
)

def str_date_to_decimal(str_date : str) -> float:
    l1, l2 = str_date.split('-')
    return (int(l1)-1)/365 + int(month[l2])/12

def datetime_to_decimal(date: datetime) -> float:
    __yr, mon, d = str(date).split(' ')[0].split('-')
    return (int(mon)-1) /12.0 + (int(d)-1) / 365.25

'''print(str_date_to_decimal('3-Feb'))

print(
    datetime_to_decimal(ex1.iat[2,1])
)'''

low_date = [*[datetime_to_decimal(ex1.iat[i, 1]) + ex1.iat[i, 0] for i in range(2, 87)]]
high_date = [*[datetime_to_decimal(ex1.iat[i, 4]) + ex1.iat[i, 0] for i in range(2, 87)]]

low_elev = [*[ex1.iat[i, 3] for i in range(2, 87)]]
high_elev = [*[ex1.iat[i, 6] for i in range(2, 87)]]

# NOTE 
_style = ''
_enable_scatter_point = 1
_enable_plot_line = 0
_legend = 1
_grid = 1

plt.style.use(_style) if _style else 0



sca1 = plt.scatter(x, y, marker='.', s=7) if _enable_scatter_point else 0
line1 = plt.plot(x, y) if _enable_plot_line else 0


plt.xticks([*[i for i in range(int(min(x)), int(max(x))+1, 5)]], fontsize=7)
plt.yticks(np.arange(int(min(y))-1, int(max(y)+1)+50, 50))

plt.title('Monthly Elevation from 1935-2021')
plt.xlabel('Year')
plt.ylabel('Elevation of Water at Lake Mead (in feet above sea level)')
plt.grid(_grid)
plt.legend([line1[0]], ['Average Elevation']) if _legend and _enable_plot_line else 0

df = pd.DataFrame(y, x)
sizes = [12, 60, 120]
colors_ = ["Red", "Yellow", "Purple"]
rolling_wins = [df.rolling(window=size_).mean() for size_ in sizes]
r_lines = [plt.plot(rolling_win, color=color_) for rolling_win, color_ in zip(rolling_wins, colors_)]
print(r_lines)
legend_lines = [k[0] for k in [*r_lines]]
legend_tags = [f'Rolling Window: size={i}' for i in sizes]

plt.legend([sca1, *legend_lines], ['Elevation', *legend_tags])if _legend and _enable_scatter_point else 0

plt.show()
print('done')


