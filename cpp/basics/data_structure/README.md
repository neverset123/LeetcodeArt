## string
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
### return 值为vector时可以直接{1,2}
### 首尾元素
vec.front(), vec.back()
### 首尾元素index
vec.begin(), vec.end()
### 弹出元素
vec.pop_back() //只能弹出最后一个元素，移除任意元素需用vec.erase()
### 翻转数组
std::reverse(vec.begin(), vec.end())
### 数组排序
std::sort(vec.begin(), vec.end())
