## aggregate, grouping, ordering
1. 找到中值并排序
```
df.groupby(["Company"])["EngineSize", "MPG"].agg("median").sort_values(by="MPG", ascending=False).reset_index()
```
2. 检测缺失值
DataFrame.notnull() 返回DataFrame中每个元素的布尔值掩码，指示元素是否不是NA值
3. transform
```
#transform可以保持与原数据集相同数量的项目
df["Order_Total"] = df.groupby('order')["ext price"].transform('sum')
```
4. merge, join 和concat
merge默认内连接，通常是重复列名做连接键；
join默认左连接，通常是行索引上的合并；
concat是直接轴向拼接

## filtering

## manipulating text
1. 结合np可以实现基于其他column的条件值
```
condlist = [num_reviews == 0, num_reviews.between(1,5),num_reviews.between(5,15),num_reviews.between(15,40),num_reviews>40]
choicelist = ['NO','FEW','SOME','MANY','A LOT']
airbnb_search_details['reviews_qualification'] = np.select(condlist,choicelist)
```
2. apply(lambda x: x)

## manipulate datetime
1. string to datetime
```
pd.to_datetime("2020-02-10")
```
2. time difference
```
from datetime import timedelta
timedelta(days=30)
```
