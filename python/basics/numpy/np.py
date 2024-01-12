import numpy as np
#获取numpy help
np.info(np.dot)

# 1. 创建ndarray, np.array是创建ndarray的高层函数，np.ndarray是底层类的构造函数
array = np.random.randint(10, size=(3,7)) #生成随机数
array = np.random.random((3,7)) #生成[0,1)之间的随机数，也可以用np.random.rand(3,7)
permutation = np.random.permutation(Y.shape[0]) #随机重新排序
array = np.zeros(12)
array = np.ones(12)
array = np.repeat(1,5)
array = np.array([np.arange(5)]*2)
array = np.linspace(0,10,5)
array_reshaped=array.reshape(2,2,3)
array[:, np.newaxis]
print(array_reshaped[:,0,1]) #打印第一行，第二列的所有元组
#对角线为1的矩阵
np.eye(3)
#对角矩阵
np.diag(1+np.arange(4), k=-1)
# 非零
np.nonzero([1,2,0,0,3,4])
#increase dimension
np.expand_dims(array, axis=0)
#转换数据类型
np.astype(int)

#使用自定义数据类型
T = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price',np.float32)])
np.array([("DVD", 42, 3.14),("Butter",13,2.72)],dtype=T)
#创建矩阵，matrix是 ndarray 的子类，只能表示二维数据
np.mat('1 2 3; 4 5 6; 7 8 9')
# matrix转ndarray
mat.A
np.asarray(mat)
#ndarray转matrix
np.asmatrix(array)
#通过c和d创建复合矩阵
np.bmat('c d;c d') 
array = s.values # pandas Series 转换为np array

# 2.改变数组维度
# 数组展平
array.ravel()
array.flatten()
#改变维度大小
array.shape=(2,3)
#将多惟array展平为一维，返回迭代器，可以用for访问每个元素
array.flat 
array.flat[[1,3]] #取展平后的第一和第三个元素
#enumerate
np.ndenumerate()

# 3. 数组组合
#水平拼接， 增加列维度
np.concatenate((a,b), axis=1)
np.hstack((a,b))
#垂直拼接，增加行维度
np.concatenate((a,b), axis=0)
np.vstack((a,b))
# 深度组合, 当数组为2维(M,N)或者一维(N,)时，首先将其维度改变为(M,N,1)、(1,N,1),然后沿着第三根轴拼接
np.dstack((a,b))
# 列组合
np.column_stack((a,b)) #将一维(N,)改变为(N,1),然后沿列拼接
np.stack((a,b), axis=1)  #axis参数指定新轴在结果尺寸中的索引, axis=0不切开，axis=1横着切开，axis=2竖着切开
# 行组合
np.row_stack((a,b)) #将一维(N,)改变为(1,N),然后沿行拼接
np.stack((a,b), axis=0)


# 3. 数组分割
#水平分割，使列维度消失，返回list
np.hsplit(a,3)
np.split(a,3,axis=1)
#垂直分割, 使行维度消失，返回list，输入至少为2维
np.vsplit(a,3)
np.split(a,3,axis=0)
#深度分割，输入至少为3维
np.dsplit(a,3)

# 4. 属性
array.dtype
array.shape
array.ndim
array.size
array.itemsize #每个元素所占字节数
array.nbytes #arry所占总字节数
array.tolist()

# 5. 读写文件
np.savetxt(fname, array, fmt='%d', delimiter=',')
c,v=np.loadtxt(fname, delimiter=',', usecols=(6,7), unpack=True) #unpack=True将每一列分别赋给不同的变量

# 6 常用函数
# 截断小数点位
np.round(c, 2)
#加权平均
np.average(c, weights=v)
#算数平均
np.mean(c)
#求序列的最值
np.max()
np.min()
np.ptp(c) #最大值与最小值之间的差值
array.argmax() #返回最大值index
#排序
np.msort(c) #按照第一个维度进行从小到大排序
np.sort(c, axis=0)
np.argsort(c,axis=0) #返回索引
#sort matrix with column
Z[Z[:,1].argsort()]
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
# 找到满足条件的元素
array[(array>3) & (array<6)]
# 取出对应索引的值
indices=[1,2]
np.take(c, indices)
# 作用函数
np.apply_along_axis(func1d=np.mean, axis=0, arr=array)
#逐位比较取其大者，最少传入两个array
np.maximum(a,b)
# 移动平均, 注意一定要invert weights
np.convolve(data, weights[::-1])
#计算指数
np.exp(c)
#用指定值填充np array
c.fill(1)
#padding数组边缘, 用于修改array尺寸
np.pad(array, pad_width, mode)
#矩阵转换
#numpy默认是row vector, 高维转置可以用arr.T;但是1D array转置只能用arr[:,None]或者np.array(features, ndmin=2).T
c.T #转置
c.I #逆矩阵
#向量化
np.vectorize(func)(args) #将只接受单个数值的func转换为接受array的函数
# count unique values in array
np.unique(array, return_counts=True)

#7.数组修剪与压缩
c.clip(3,7) #将c中小于3的设为3， 大于7的设为7
c.compress([False, True, True], matrix, axis=0) #选取某一维度的切片
np.prod(c) #计算c中所有元素的乘积

# 8.相关性
np.conv(X,Y) #计算a和c之间的协方差矩阵
c.diagonal() #获取c对角线上的元素
c.trace() #对角线上元素之和
np.corrcoef(X, Y) #计算a和c之间的相关系数(X、Y的协方差除以X的标准差和Y的标准差)

#9. agg通用函数
np.add.reduce(a, axis=0) #对数组元素求和
np.add.accumulate(a, axis=0) #累加求和
# when i = len(indices) - 1 (so for the last index), indices[i+1] = array.shape[axis].
# if indices[i] >= indices[i + 1], the i-th generalized “row” is simply array[indices[i]].
# if indices[i] >= len(array) or indices[i] < 0, an error is raised.
np.add.reduceat(a, [0, 5, 2, 7]) #计算索引间的累加, add可以替换为multiply等其他ufunc
#将第一个列表或数组中的每个元素依次加到第二个列表或数组中的每个元素，得到每一行
np.add.outer(np.arange(3), a)

#10. 算术运算
# 逐元素进行算术运算
np.add
np.subtract
np.multiply
np.divide
# 返回整数结果，相当于先divide再取floor
np.floor_division 
#模运算
np.mod
#取余
np.remainder
#数学运算
R = np.sqrt(X**2+Y**2)
T = np.arctan2(Y,X)
##叉乘， 点乘
np.cross(a,b)
np.dot(a,b)
#np.nan is not comparable to np.nan
np.nan == np.nan #return False
np.isnan(np.nan) #return True

#11 线性代数
#线性拟合
A=np.vstack([x,np.ones(len(x))]).T
k,b=np.linalg.lstsq(A,y)
#多项式拟合
poly=np.polyfit(x, y, 3) #三项式拟合
np.polyval(poly, x) #预测
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
#左右翻转
np.fliplr(array)
#归一化
array_random=np.random.random((5,5))
zmax, zmin=array_random.max(), array_random.min()
print((array_random-zmin)/(zmax-zmin))
#两数组交集元素
np.intersect1d(array1, array2)

#12 筛选数据
condlist = [num_reviews == 0, num_reviews.between(1,5),num_reviews.between(5,15),num_reviews.between(15,40),num_reviews>40]
choicelist = ['NO','FEW','SOME','MANY','A LOT']
np.select(condlist,choicelist)

X_selected = array[np.argwhere(array1==1)] #用array1去筛选array


