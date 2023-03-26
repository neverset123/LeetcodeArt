class Solution:
    def maxA(self,m):
        dp=[0]*(m+1)
        for i in range(1, m+1):
            dp[i]=dp[i-1]+1
            for j in range(2, i):
                dp[i]=max(dp[i], dp[j-2]*(i-j+1))
        return dp[m]

if __name__ == "__main__":
    m=7
    solution=Solution()
    print(solution.maxA(m))