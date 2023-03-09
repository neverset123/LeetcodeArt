#dp记录在状态(i，j)下已进行的操作数
#有错误不知道为啥
import sys
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        memo=[[sys.maxsize]*(len(s2))]*(len(s1))

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