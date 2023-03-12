from typing import List
import sys

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*(n) for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j]=min(dp[i][j-1]+grid[i][j],
                            dp[i-1][j]+grid[i][j])
        return dp[m-1][n-1]
    
    
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        memo=[[-1]*n for _ in range(m)]
        #从 grid[i][j] 到达终点（右下角）所需的最少生命值是 dp(grid, i, j)
        def dp(dungeon, i, j):
            if i==m-1 and j==n-1:
                return 1 if dungeon[i][j]>=0 else abs(dungeon[i][j])+1
            if i==m or j==n:
                return sys.maxsize
            if memo[i][j]!=-1:
                return memo[i][j]
            #倒序找到所需最少生命值的路径
            res=min(dp(dungeon, i+1, j), dp(dungeon, i, j+1))-dungeon[i][j]
            memo[i][j]=1 if res<=0 else res
            return memo[i][j]
        print(memo)
        return dp(dungeon, 0, 0)
       
