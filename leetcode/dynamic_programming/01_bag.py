#对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值是 dp[i][w]
##分为完全背包和子集背包
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        sums=sum(nums)//2 #整除要用//
        dp=[[False]*(sums+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=True
        for i in range(1, len(nums)+1):
            for j in range(1, sums+1):
                if j<nums[i-1]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j]
        return dp[len(nums)][sums]

    def change(self, amount: int, coins: List[int]) -> int:
        m=len(coins)
        dp=[[0]*(amount+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for i in range(1, m+1):
            for j in range(1, amount+1):
                if coins[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i-1]] ## 注意完全背包的重复利用
        return dp[m][amount]



