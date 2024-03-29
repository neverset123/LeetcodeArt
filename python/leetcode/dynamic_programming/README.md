## 判断动态规划
* 符合最优子结构(子问题之间必须互相独立)
* 重叠子问题

## 思路
明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。
## 框架
#自顶向下递归的动态规划(定义dp函数)
#定义备忘录
memo=[]
def dp(状态):
    base_case
    检测备忘录memo
    for 选择 in 所有可能的选择:
        # 此时的状态已经因为做了选择而改变
        result = 求最值(result, dp(状态))
    更新备忘录memo
    return result

#自底向上迭代的动态规划(定义dp数组)
#定义数组
dp=[[0]*dim1 for _ in range(dim2)]
#初始化 base case
dp[0][0][...] = base case
#进行状态转移
for 状态 in 状态的所有取值：
    dp[状态1][状态2][...] = 求最值(选择1，选择2...)
#找到要返回的状态

## 回溯和动态规划
回溯就是遍历，复杂度高;动态规划是解决重复子问题，效率高

```
#斜向遍历
for l in range(2, n+1):
    for i in range(n):
        j = l+i-1
        dp[i][j]=...
```