### 检查前一命令是否执行成功
```
$?
```
### 读取用户输入
```
read
```
### case 
```
case EXPRESSION in
  PATTERN_1)
    STATEMENTS
    ;;
  PATTERN_2)
    STATEMENTS
    ;;
  PATTERN_N)
    STATEMENTS
    ;;
  *)
    STATEMENTS
    ;;
esac
```
### 算术运算
```
expr 5 + 2
=$[16 + 4]
```
### 比较
1）数字
```
test 1 -eq 2 && echo “true” || echo “false”
[ 1 -eq 2 ] && echo “true” || echo “false”
```
2）字符串
```
[ “hello world” != “Hello World” ] && echo “true” || echo “false”
```
3）文件
-d 文件名    如果文件存在并且是目录，返回true
-e 文件名    如果文件存在，返回true
-f 文件名    如果文件存在并且是普通文件，返回true
-r 文件名    如果文件存在并可读，返回true
-s 文件名    如果文件存在并且不为空，返回true
-w 文件名    如果文件存在并可写，返回true
-x 文件名    如果文件存在并可执行，返回true
```
[ -s /bin/bash ] && echo $?
```





