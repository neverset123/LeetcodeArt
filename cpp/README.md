## bazel
当前项目由bazel构建
```
# add 'C:\msys64\mingw64\bin' and 'C:\MinGW\bin' to PATH
# set BAZEL_SH to  'C:\msys64\usr\bin\bash.exe'
bazel run :example

# build debug
# cd  C:\msys64\mingw64\x86_64-w64-mingw32\lib\
# strip -d crt2.o
# gcc basics\main.cpp -o main.exe -lstdc++ -g
# dgb main.exe
bazel build -c dbg :example
```
## c++ 17
C++11 标志着现代 C++的开端，C++14 在 11 的基础上查缺补漏，并未加入许多新特性，而 C++17 作为 C++11 后的第一个大版本，标志着现代 C++逐渐走向成熟。
- 语法糖
- 结构化绑定
- std::tuple 的隐式推导
- if 初始化语句
- std::string_view
- std::any: 相比于void*更安全
- 强制执行copy elision

## 算法
算法的本质就是**穷举**，这点跟数学是不一样的。
### 如何穷举？
找状态转移方程才是难点，递归穷举的核心是数学归纳法，明确函数的定义，然后利用这个定义写递归函数，就可以穷举出所有可行解。
### 如何聪明地穷举？
非递归算法技巧:
- 贪心算法：在题目中发现一些规律（贪心选择性质），使得不用完整穷举所有解就可以得出答案，效率比动态规划还高
- 双指针
    - 二分搜索技巧: 只能运用在有序数组上
    - 滑动窗口技巧: 只能运用在扩大缩小窗口的条件明确的情况下
    - 回文串技巧
    - 前缀和技巧
    - 差分数组技巧
- 二叉树
    - 回溯算法：遍历
    - 动态规划：分解问题计算答案，有「最优子结构」和「重叠子问题」两个特性，而且一定是让你求最值的
    - 分治算法：只有子结构，没有重叠子问题，不能用备忘录去优化
    - BFS：层序遍历

