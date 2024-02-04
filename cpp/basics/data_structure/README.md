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

