## string
### Streaming
istringstream str(a);
### 字符转字符串
char c = 'a';
std::string str(1, c);
### 添加和删除字符
str.push_back("a")
str.pop_back()
### 添加字符串
str.append("abc")
### 遍历字符串字符
for(char c: str)

## queue
### 入列和出列
q.push("a")
q.pop()

### 访问队首和队尾元素
q.front()
q.back()

## map
### 使用方括号访问键值，如果key不存在，那么会自动创建这个Key，并赋值为0

### 检查键值是否存在
map.count(key) 

## vector
函数内部vector可以作为返回值，因为cpp自动处理内存管理问题。
```
vector<int> vec={1,2}
vec.at(index)
vec.front(), vec.back() 
vec.begin(), vec.end()
vec.push_back(3);
vec.pop_back() //只能弹出最后一个元素，移除任意元素需用vec.erase()
std::reverse(vec.begin(), vec.end()) //翻转数组
std::sort(vec.begin(), vec.end()) //排序数组
```
### cbegin和begin
- cbegin返回一个指向容器第一个元素的const迭代器，无论容器是否为const，返回的迭代器都是不可修改容器元素的
- begin返回一个指向容器第一个元素的迭代器。如果容器是非const的，那么返回的迭代器是可修改容器元素的。如果容器是const的，那么返回的迭代器是不可修改容器元素的

## VectorXd/MatrixXd
两者都是Eigen库中的数据类型，用于表示向量和矩阵。"X"表示这是一个动态大小的数据结构，"d"表示它存储的是双精度浮点数（double）。Eigen还提供了其他类型的向量和矩阵，如Vector3f（一个包含三个浮点数的向量）和Matrix4i（一个4x4的整数矩阵）
```
Eigen::VectorXd vec(3); // create a vector with 3 elements
vec << 1, 2, 3; // assign values to the vector
Eigen::MatrixXd mat(2, 2); // create a 2x2 matrix
mat << 1, 2,
       3, 4; // assign values to the matrix
```



