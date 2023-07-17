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


