回溯算法就是个多叉树的遍历问题
回溯算法就是纯暴力穷举，复杂度一般都很高

## 框架
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择