1.const
作用: 定义常量，防止修改。
const对象默认为文件局部变量，需用extern 显式修饰才能在文件外访问
1）指向常量的指针
不能使用void*指针保存const对象的地址，必须使用const void*类型的指针保存const对象的地址
2）常指针
const指针必须进行初始化，且const指针的值不能修改。
