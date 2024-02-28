import seaborn as sns


## decorations
gridobj.set(xlim=(0, 60), ylim=(0, 12), xticks=[10, 30, 50], yticks=[2, 6, 10])

## subplot layout
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)


## scater with linear regression
sns.lmplot(x='x', y='y', data=data, fit_reg=True)
sns.stripplot(x='x', y='y', data=data, jitter=True) # one variable is categorical

## density plot
sns.kdeplot(data.x, data.y, cmap='Blues', shade=True, bw=.15)
sns.displot(data.x, kde=True, bins=30)

## regression plot
sns.regplot(x=x, y=y)

## heatmap
sns.heatmap(glue, annot=True, fmt=".1f")

## EDA
## 分类绘制数据分布图,可以通过kind参数设置图形类型(strip,swarm,box,violin,boxen,point,bar,count)
sns.catplot(x='income', y='capital-gain', hue='sex', data=data, kind='bar')

## pairgrid和facetgrid
## 用于绘制多个变量之间的关系图
iris = sns.load_dataset("iris")
g = sns.PairGrid(iris, hue="species", palette=sns.color_palette("cubehelix", 3), vars=['sepal_length','sepal_width','petal_length','petal_width'])
g.map(plt.scatter) # 可以使用plt或者sns中的绘图函数
#g.map_diag(plt.hist) # 对角线上的图形类型
#g.map_offdiag(plt.scatter) # 非对角线上的图形类型
plt.show()

g = sns.FacetGrid(iris, row="sepal_length", col="species", hue="sepal_width", margin_titles=True)
g.map(plt.scatter, "sepal_length", "sepal_width")
g.add_legend()
plt.show()

## countplot
sns.countplot(x="species", data=iris)
plt.show()


