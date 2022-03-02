import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
from sklearn.preprocessing import LabelEncoder
from numpy import sin
import seaborn as sns

x = np.linspace(0, 10, 100)
y = sin(x)
z = np.cos(x)

fig1 = pyplot.figure(figsize=(10, 7))
pyplot.subplot(2, 2, 1)
pyplot.title("Data 1 ")
pyplot.plot(x, y, color='red', linestyle="dashed", linewidth=4)

pyplot.xlabel("x")
pyplot.ylabel("sin(x)")
pyplot.legend(("x", "sin(x)"))
pyplot.subplot(2, 2, 2)
pyplot.title("Data 2 ")
pyplot.plot(x, z)

pyplot.xlabel("x")
pyplot.ylabel("cos(x)")
pyplot.legend(("x", "cos(x)"))
pyplot.show()
# scatter
iris = sns.load_dataset("iris")

# sns.lineplot(data=iris, y="petal_width", x=iris.index, hue='species')
fig1 = pyplot.figure(figsize=(10, 8))
pyplot.subplot(2, 2, 1)
pyplot.scatter(iris['petal_width'], iris['petal_length'])
pyplot.title("pw/pl")
pyplot.subplot(2, 2, 2)
pyplot.scatter(iris['sepal_length'], iris['petal_length'])
pyplot.title("sl/pl")
pyplot.subplot(2, 2, 3)
pyplot.scatter(iris['sepal_length'], iris['petal_width'])
pyplot.title("sl/pw")
pyplot.subplot(2, 2, 4)
pyplot.scatter(iris['sepal_length'], iris['sepal_width'])
pyplot.title("sl/sw")
fig1.savefig("fig")
pyplot.show()

# bar plot

iris = sns.load_dataset("iris")

data = iris.groupby("species").mean()['petal_length']
ax = sns.barplot(x=data.index, y=data.values)
pyplot.show()

# hist plot

iris = sns.load_dataset("iris")

sns.histplot(data=iris, x='petal_length', hue='species', bins=25)
pyplot.show()


# pie plot


iris = sns.load_dataset('iris')
iris = iris.groupby("species").mean()['petal_length']
labels = ['a', 'b', 'c']
pyplot.pie(iris, labels=labels)
pyplot.show()
