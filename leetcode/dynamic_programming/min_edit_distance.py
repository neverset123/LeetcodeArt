#dp记录在状态(i，j)下已进行的操作数

import sys
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        memo=[[sys.maxsize]*(len(s2)) for _ in range(len(s1))]

        def dp(s1, s2, i, j):
            if i==-1:
                return j+1
            if j==-1:
                return i+1
            print(i,j)
            if memo[i][j]!=sys.maxsize:
                return memo[i][j]
            if s1[i]==s2[j]:
                memo[i][j]=dp(s1,s2,i-1, j-1)
            else:
                memo[i][j]=min(
                    #delete i
                    dp(s1,s2,i-1,j)+1,
                    #insert i
                    dp(s1,s2,i,j-1)+1,
                    #replace
                    dp(s1,s2,i-1,j-1)+1
                )
            return memo[i][j]
        
        return dp(s1,s2,len(s1)-1, len(s2)-1)
    
    def minDistance(self, s1: str, s2: str) -> int:
        m,n=len(s1),len(s2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            dp[i][0]=i
        for j in range(1, n+1):
            dp[0][j]=j
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,
                                     dp[i][j-1]+1,
                                     dp[i-1][j-1]+1)
        return dp[m][n]
    
    
