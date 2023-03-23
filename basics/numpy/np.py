import numpy as np

#创建array
array = np.zeros(12)
array_reshaped=array.reshape(2,6)
print(array_reshaped)
print(array_reshaped[0,1])
print(array_reshaped[(array_reshaped>3) & (array_reshaped<6)])

#获取memory size
array_2d = np.zeros((10,10))
print(array_2d.size*array_2d.itemsize)

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

