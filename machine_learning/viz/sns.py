## EDA
import seaborn as sns
sns.catplot(x='income', y='capital-gain', hue='sex', data=data, kind='bar')

## pairgrid
import seaborn as sns
import matplotlib.pyplot as plt
g = sns.PairGrid(iris, hue="species", palette=sns.color_palette("cubehelix", 3), vars=['sepal_length','sepal_width','petal_length','petal_width'])
g.map(plt.scatter)
plt.show()

## countplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x="species", data=iris)
plt.show()


