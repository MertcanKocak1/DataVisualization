import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import mkdir

try:
    mkdir("Plots")
except:
    pass
mypath = "Plots"
sns.set(rc={'figure.figsize': (5, 5)})
# data reading
df = pd.read_csv('world-happiness-report.csv')
f, axes = plt.subplots(5, 2, figsize=(15, 20))
# padding
f.tight_layout(pad=8)
f.suptitle('Distrubution before preprocessing')
# drop 'object' type data column
cols = df.select_dtypes(exclude="object").columns
x_axis = 0
y_axis = 0
for col in cols:
    # for hist
    # sns.histplot(data=df, x=col, kde=True, ax=axes[x_axis, y_axis])
    sns.boxplot(data=df, x=col, ax=axes[x_axis, y_axis])
    axes[x_axis, y_axis].set_xlabel(col.title())
    axes[x_axis, y_axis].set_ylabel(col.title())
    axes[x_axis, y_axis].set_title(f"{col.title()} Count")

    if y_axis == 1:
        y_axis = 0
        x_axis += 1
    else:
        y_axis += 1

#
# year_group = df.groupby('year').sum()
# year_group['Positive affect'].plot()

#year_group = df.groupby('year').sum()
# year_group['Negative affect'].plot()
#ax1 = sns.barplot(x=year_group.index, y=year_group['Social support'].values)
#ax1.tick_params(axis='x', rotation=90)

#Heat Map
#
#sns.heatmap(data.corr(), annot = True)
plt.savefig(f"{mypath}/boxplot.png")
plt.show()
