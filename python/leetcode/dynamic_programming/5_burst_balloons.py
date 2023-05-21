# max coins can be got by bursting balloons

from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        m=len(nums)
        # 加入边界
        temp_nums=[1]+nums+[1]
        # dp[i][j]表示戳破(i,j)的气球可以获得的最高分数
        dp=[[0]*(m+2) for _ in range(m+2)]
        # 从下到上遍历状态i,j
        for i in range(m+1, -1, -1):
            for j in range(i+1, m+2):
                # i和j之间最后戳破的气球为k
                for k in range(i+1, j):
                    dp[i][j]=max(dp[i][j], dp[i][k]+dp[k][j]+temp_nums[i]*temp_nums[k]*temp_nums[j])
        return dp[0][m+1]
