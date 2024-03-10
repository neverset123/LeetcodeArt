import pandas as pd
import numpy as np

#创建数据
data_dict = {} #键值为列索引，值可以为Series或dict
data_list = []
df = pd.DataFrame(data_dict)
df["col"] = np.array()
df["col"] = [1,2,3]
df = pd.DataFrame([[1,2]]*4, columns=['A', 'B'])
df = pd.read_csv(filename)
df = pd.read_table(filename) #读取文本
df = pd.read_excel(filename, header=1)
df = pd.read_sql(filename)
df = pd.read_json(filename)
df = pd.read_html(filename)
df = pd.json_normalize(a_dict) #将字典或者nested字典导入pandas
s = pd.Series(data_list)
df = s.to_frame()
df = pd.date_range(start='2018/01/01', end='2018/07/01', freq='M') 
df["year"] = s.dt.year #dt函数获取year, month, day, hour


#导出数据
df.to_csv(filename, compression='gzip') # save with compression
df.to_excel(filename)
df.to_sql(table_name,connection_object)
df.to_json(filename)
writer=pd.ExcelWriter('test.xlsx',index=False) 
df.to_excel(writer,sheet_name='sheet1')
writer.save()
data_dict = df.to_dict("records") #将DataFrame转换为字典列表
yaml.dump(data_dict, open("data.yaml", "w"), sort_keys=False) #将DataFrame转换为yaml格式

#查看数据
df.head(n) # 查看DataFrame对象的前n⾏
df.tail(n) # 查看DataFrame对象的最后n⾏
df.shape() # 查看⾏数和列数
df.info() # 查看索引、数据类型和内存信息
df.columns() # 查看字段（⾸⾏）名称
df.describe() # 查看数值型列的汇总统计
s.astype(float) #转换数据类型，节省内存
df.set_index('column_one') # 将某个字段设为索引，可接受列表参数，即设置多个索引
df.reset_index("col1") # 将索引设置为col1字段，并将索引新设置为0,1,2...
df.nunique(axis=0) #unique count in axis

for index, row in df.iterrows(): #遍历
    print(f'Index: {index}, row: {row.values}') # row.values将不同column的数值组合为array
    #only print column_a
    print(f'Index: {index}, column_a: {row.get("column_a", 0)}')

for row in df.itertuples(): #迭代器
    print(row)

#选取数据
df[col_name] #返回一列（series）
df[[col_name1, col_name2]]
s.iloc[0]
s.loc['index_name']
df.iloc[0,:] #loc是按索引,iloc参数只接受数字参数
df.loc[0,:]
df.at[5, "col1"]
df.iat[5,0]
df.isnull()
df.notnull()

#处理数据
df.columns = ['a','b','c'] #重命名列名
df.dropna() # 删除所有包含空值的⾏
df.dropna(axis=1,thresh=n) # 删除所有⼩于n个⾮空值的⾏
df.fillna(value=x) # ⽤x替换DataFrame对象中所有的空值
df.replace(1,'one') # ⽤‘one’代替所有等于1的值
df.replace([1,3],['one','three']) # ⽤'one'代替1，⽤'three'代替3
df.rename(columns=lambda x:x+1) # 批量更改列名
df.rename(columns={'old_name':'new_ name'}) # 选择性更改列名
df.rename(index=lambda x:x+1) # 批量重命名索引
df.insert(0, 'category', ['cat1','cat2','cat3']) #插入数据
pd.melt(df, id_vars='category') #行列转换
df.stack()#重组列和行, 回复原状用.unstack()
df.drop(['E','F','G'], axis=1, inplace=True) #删除列
df.drop([3], axis=0, inplace=True) #删除行

df.applymap(lambda x:"%.2f" % x)  #对每个元素应用函数
df["gender"].map({"man":1, "women":0}) #转换数据标签

df['Close*'].gt(df['Open']) #逻辑运算

#特征处理
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
imp = SimpleImputer(missing_values=np.nan, strategy="median")
scaler = MinMaxScaler()
df_imp = pd.DataFrame(imp.fit_transform(df), columns=df.columns)
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
df.apply(lambda x: np.log(x)) #用log处理倾斜数据

#数据统计
df.sort_index() #进⾏索引排序
df.sort_values(col1, ascending=False) # 按照列col1排序数据，默认升序排列
df.sort_values([col1,col2],ascending=[True,False])  # 先按列col1升序排列，后按col2降序排列数据

s.value_counts(dropna=False)  # 查看Series对象的唯⼀值和计数, 可以用于Frequency Encoding

df.groupby(col1)[col2].agg("mean") #df.groupby(col1)[col2].agg(np.mean), agg可以接受 "median"
df.groupby(col1).col2.transform("sum") # 通常与groupby连⽤，避免索引更改
df.pivot_table(index=col1,values=[col2,col3],aggfunc={col2:"max",col3:["max","min"]}) # 创建⼀个按列col1进⾏分组，计算col2的最⼤值和col3的最⼤值、最⼩值的数据透视表

df.apply(pd.Series.value_counts) # 查看DataFrame对象中每⼀列的唯⼀值和计数
df.apply(np.mean) #对DataFrame中的每⼀列应⽤函数np.mean
df.apply(np.max,axis=1, raw=False) # 对DataFrame中的每⼀⾏应⽤函数np.max, raw=false传递到func为Series，raw=true传递参数为ndarray
df.apply(lambda x: x[0:2])

s.corr(s1)  # 计算Series对象s和s1之间的相关系数

#合并数据
# merge默认内连接，通常是重复列名做连接键；
# join默认左连接，通常是行索引上的合并；
# concat是直接轴向拼接
df.append(df1) #按行合并
pd.concat([df1,df2],axis=1,join='inner') # 将df2中的列添加到df1的尾部,值为空的对应⾏与对应列都不要
df.join(df2,on=col1,how='inner')
pd.merge(df1,df2,on='col1',how='outer') # 对df1和df2合并，按照col1，⽅式为outer
pd.merge(df1,df2,left_index=True,right_index=True,how='outer') #与 df1.join(df2, how='outer')效果相同
pd.merge(df1, df2, left_on='id', right_on='number')

#高性能运算
#eval和query 能够在没有任何中间内存开销的情况下直接获得C语言级别的运算速度,他们底层都调用了Numexpr包
df.query('(age > 25) & (height > 165) & (gender == "female")')
df.query('(age > @min_age) & (height > @min_height) & (gender == @g)')
df.eval('D = (A + B) / C', inplace=True)
df.eval('A + @column_mean')


#操作字符串
s.str.upper()
s.str.lower()
s.str.strip()
s.str.len() #读取每个元素字符串长度
s.str.cat(sep=" ")
s.str.replace('the', 'a')
s.str.split()
s.str.count('a')
s.str.startswith('a')
s.str.endswith('d')
cities = ['New York', 'Rome', 'Madrid', 'Istanbul', 'Rome']
pd.Series(cities).str.get_dummies() #将标签one-hot化, 也可以用replace或map实现
pd.get_dummies(df) #自动将非数值数据转换为one-hot形式，同时保留数据数据
s_encoded = (s == "yes").astype(int) #将二分类标签转换为数值标签
df['wt_cat_cut'] = pd.cut(np.array(df['weight']), 4, labels=["Light", "Medium", "Heavy", "Very heavy"])

#sql



#搭建流水线
df.pipe(func)


#绘图
#绘图是基于matplotlib实现的
df.plot.bar()
df.plot.barh()
df.plot.kde() #绘制密度曲线

df.plot.hist()
s.hist()
df.plot.box()
df.plot.scatter()

df.plot(subplots=True, layout=(1,2)) #subplot