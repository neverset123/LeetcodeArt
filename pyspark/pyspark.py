## 创建df或rdd
#直接生成的RDD中的元素通常是基本数据类型（如 int、float、string 等）或它们的组合（如 tuple、list、dict 等）。
# DataFrame转换得到的RDD中的元素是Row对象，每个Row对象代表DataFrame中的一行,
#需要先使用 rdd.map(lambda row: (row["column1"], row["column2"])) 的操作来将Row对象转换为更容易处理的数据结构（如 tuple）
from pyspark.sql import Row
df = spark.read.csv('data.csv', header=True, inferSchema=True)
df = spark.createDataFrame([("a", 1), ("b", 2)], ["letter", "number"])
df = spark.createDataFrame([Row(a=1, b=2, c=3), Row(a=4, b=5, c=6)])
rdd = df.rdd    # 转换为rdd

data = [("Alice", 1, 2), ("Bob", 3, 4), ("Charlie", 5, 6)]
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(["name", "age", "height"])

df.cache() # 缓存
df.unpersist() # 取消缓存
rdd.cache() # 缓存
rdd.unpersist() # 取消缓存

## indexing
df.first() # 返回第一行
df.take(2) # 返回前两行
df.first()[0] # 返回第一行的第一个元素
df.sample(False, 0.1) # 采样

rdd.first() # 返回第一个元素
rdd.take(2) # 返回前两个元素
rdd.first()[0] # 返回第一个元素的第一个元素
rdd.sample(False, 0.1) # 采样

## 合并数据
df1.union(df2) # 行合并
df1.join(df2, df1["col1"] == df2["col1"], "inner") # 列合并， inner, outer, left, right 默认inner

rdd1.union(rdd2) # 行合并
rdd1.join(rdd2) # 列合并，按照键值进行合并

## 排序
df.sort(df["col1"].desc()) # 按照col1降序排序， 默认升序
df.sort("col1", "col2") # 按照col1升序，col2升序排序

rdd.sortBy(lambda row: row["col1"], ascending=False) # 按照第一列降序排序， 默认升序
rdd.sortBy(lambda row: (row["col1"], row["col2"])) # 按照第一列升序，第二列升序排序

## 过滤
df.filter(df["col1"] > 1) # df使用条件表达式过滤
df.filter("col1 > 1") # df使用字符串过滤

df.rdd.filter(lambda row: row["col1"] > 1) # rdd使用函数过滤

## 统计
df.agg(F.sum("col1"), F.mean("col1"), F.max("col1"), F.count("col1")) # 一次性统计多个指标(整个df)
df.groupBy("col1").agg(F.sum("col2"), F.mean("col2"), F.max("col2"), F.count("col2")) # 按照col1分组统计多个指标

df.rdd.map(lambda row: (int(row["col1"]))).sum() # 第一列求和
df.rdd.map(lambda row: (int(row["col1"]))).mean() # 第一列求均值
df.rdd.map(lambda row: (int(row["col1"]))).max() # 第一列求最大值
df.rdd.map(lambda row: (int(row["col1"]))).count() # 第一列求频数

df.rdd.map(lambda row: (row["col1"], 1)).reduceByKey(lambda x, y: x + y) # 将每一个键值对的值相加，比groupByKey更高效
df.rdd.map(lambda row: (row["col1"], 1)).groupByKey().mapValues(lambda x: sum(x)) # 按照键值对的键分组，再将每一组的值相加
df.rdd.map(lambda row: (row["col1"], 1)).reduceByKey(lambda x, y: x if x > y else y) # 按照键值对的键分组，再将每一组的值取最大值

accum = spark.sparkContext.accumulator(0) # 创建累加器
rdd.foreach(lambda row: accum.add(row["col1"])) # 使用累加器
accum.value # 获取累加器的值

## F函数
from pyspark.sql import functions as F
df.select(F.col("col1").alias("new_col1")) # 选择列，并重命名
df.select(F.col("col1").cast("int")) # 类型转换
df.select(F.col("col1").isNull()) # 判断是否为空
df.select(F.col("col1").between(1, 2)) # 判断是否在区间内
df.select(F.col("col1").like("a%")) # 判断是否匹配
df.select(F.col("col1").substr(1, 2)) # 截取字符串

df.withColumn("new_col1", F.when(df["col1"] > 1, 1).when(df["col1"] < 1, -1).otherwise(0)) # 条件选择
df.withColumn("new_col1", F.concat(df["col1"], df["col2"])) # 字符串拼接
df.withColumn("new_col1", F.lit(1)) # 添加常数列
df.withColumn("new_col1", F.col("col1") + F.col("col2")) # 列运算


## udf
#Pandas UDF性能优于UDF。
from pyspark.sql.types import IntegerType
import pandas as pd

@F.udf(IntegerType())
def udf_func(x):
    return x + 1

@F.pandas_udf(IntegerType())
def pandas_udf_func(df):
    return pd.Series(df + 1)

## sql（适合结构化的数据）
df.createOrReplaceTempView("table1") # 注册临时表
spark.sql("select * from table1 where col1 > 1") # 执行sql语句


