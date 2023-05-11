import numpy as np

# 1. 创建array
array = np.zeros(12)
array = np.ones(12)
array_reshaped=array.reshape(2,2,3)
print(array_reshaped)
print(array_reshaped[:,0,1]) #打印第一行，第二列的所有元组
print(array_reshaped[(array_reshaped>3) & (array_reshaped<6)])
#或者
np.array([np.arange(5), np.array(5)])
#使用自定义数据类型
T = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price',np.float32)])
np.array([("DVD", 42, 3.14),("Butter",13,2.72)],dtype=T)
#创建矩阵，矩阵是 ndarray 的子类
np.mat('1 2 3; 4 5 6; 7 8 9')
np.bmat('c d;c d') #通过c和d创建复合矩阵



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
# 截断小数点位
np.round(c)
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
#标准差
np.std(c)
#相邻元素差
np.diff(c)
#取对数
np.log(c)
# 找到满足条件的索引值
np.where(c>0)
# 取出对应索引的值
np.take(c, indices)
# 作用函数
np.apply_along_axis()
#选取a,b,c三个数中最大的
np.maximum(a,b,c)
# 移动平均
np.convolve(weights, c)
#计算指数
np.exp(c)
#用指定值填充np array
c.fill(1)
#矩阵转换
c.T #转置
c.I #逆矩阵


#7.数组修剪与压缩
c.clip(3,7) #将c中小于3的设为3， 大于7的设为7
c.compress(conditions) #选取某一维度的切片
np.prod(c) #计算c中所有元素的乘积

# 8.相关性
np.conv(a,c) #计算a和c之间的协方差矩阵
c.diagonal() #获取c对角线上的元素
c.trace() #对角线上元素之和
np.corrcoef(a, c) #计算a和c之间的相关系数

#9. 通用函数
np.add.reduce(a) #对数组元素求和
np.add.accumulate(a) #累加求和
np.add.reduceat(a, [0, 5, 2, 7]) #计算索引间的累加
np.add.outer(np.arange(3), a) #返回一个数组，它的秩（rank）等于两个输入数组的秩的和

#10算术运算
np.add
np.subtract
np.multiply
np.divide
np.floor_division 
#模运算
np.mod
np.remainder

#11 线性代数
#线性拟合
np.linalg.lstsq(A,c)
#多项式拟合
poly=np.polyfit(t, y, 3) #三项式拟合
np.polyval(poly, t[-1] + 1) #预测下一个值
np.roots(poly)  #多项式的根
np.polyder(poly) #多项式求导
#numpy.linalg 模块
np.linalg.inv(A) #求解逆矩阵
np.linalg.solve(A, b) #求解线性方程组Ax=b
np.linalg.eigvals(A) #求解特征值
eigenvalues, eigenvectors = np.linalg.eig(A) #求解特征值和特征向量
U, Sigma, V = np.linalg.svd(A, full_matrices=False)# 用svd() 函数分解矩阵
pseudoinv = np.linalg.pinv(A) #计算矩阵广义逆
np.linalg.det(B) #计算矩阵行列式



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