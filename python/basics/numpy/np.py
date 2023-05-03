import numpy as np

# 1. 创建array
array = np.zeros(12)
array_reshaped=array.reshape(2,2,3)
print(array_reshaped)
print(array_reshaped[:,0,1]) #打印第一行，第二列的所有元组
print(array_reshaped[(array_reshaped>3) & (array_reshaped<6)])
#或者
np.array([np.arange(5), np.array(5)])
#使用自定义数据类型
T = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price',np.float32)])
np.array([("DVD", 42, 3.14),("Butter",13,2.72)],dtype=T)

# 2.改变数组维度
# 数组展平
arr.ravel()
arr.flatten()
#改变维度大小
arr.shape=(2,3)

# 3. 数组组合
#水平拼接， 增加列维度
np.concatenate((a,b), axis=1)
np.hstack((a,b))
#垂直拼接，增加行维度
np.concatenate((a,b), axis=0)
np.vstack((a,b))
# 深度组合
np.dstack((a,b))
# 列组合
np.column_stack((a,b))
np.stack((a,b), axis=1)  #axis参数指定新轴在结果尺寸中的索引, axis=0不切开，axis=1横着切开，axis=2竖着切开
# 行组合
np.row_stack((a,b))
np.stack((a,b), axis=0)

# 3. 数组分割
#水平分割，使列维度消失，返回list
np.hsplit(a,3)
np.split(a,3,axis=1)
#垂直分割, 使行维度消失，返回list
np.vsplit(a,3)
np.split(a,3,axis=0)
#深度分割
np.dsplit(a,3)


# 4. 属性
a.dtype
a.shape
a.ndim
a.size
a.itemsize
a.nbytes
c.flat #将多惟array展平为一维
c.flat[[1,3]] #取展平后的第一和第三个元素
c.tolist()

# 5. 读写文件
np.savetext(file_name, array)
c,v=np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)

# 6 常用函数
#加权平均
np.average(c, weights=v)
#算数平均
np.mean(c)
#最大最小
np.max()
np.min()
np.ptp(c) #最大值与最小值之间的差值
#排序
np.msort(c)
#方差
np.var(c)



#获取numpy help
#np.info(np.dot)

#非零元素
print(np.nonzero([1,2,0,0,3,4]))

#对角线为1的矩阵
print(np.eye(3))

#添加padding
#np.pad

#对角矩阵
print(np.diag(1+np.arange(4), k=-1))

#归一化
array_random=np.random.random((5,5))
zmax, zmin=array_random.max(), array_random.min()
print((array_random-zmin)/(zmax-zmin))


#交集元素
#np.intersect1d

#Cartesian to pole coordinates
Z = np.random.random((10,2))
X,Y = Z[:,0], Z[:,1]
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
print (R)
print (T)


#increase dimension
#np.increse_dims

#转换数据类型
np.astype()

#enumerate
np.ndenumerate()

#sort matrix with column
Z[Z[:,1].argsort()]

##叉乘， 点乘
np.cross
np.dot

# 限制元素大小
np.clip(a, a_min, a_max)

# reshape array
array.reshape(-1, 1)
array[:, np.newaxis]