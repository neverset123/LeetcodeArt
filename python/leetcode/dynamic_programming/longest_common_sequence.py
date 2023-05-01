#对于两个字符串求子序列的问题，都是用两个指针i和j分别在两个字符串上移动，大概率是动态规划思路

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        memo=[[-1]*n for _ in range(m)]
        #dp 返回值是s1[0:i]和s2[0:j]的最长公共子序列长度
        def dp(s1,s2,i,j):
            if i==-1 or j==-1:
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            if s1[i]==s2[j]:
                memo[i][j]=dp(s1,s2,i-1,j-1)+1
            else:
                memo[i][j]=max(dp(s1,s2,i-1,j), dp(s1,s2,i,j-1), dp(s1,s2,i-1,j-1))
            return memo[i][j]
        res=dp(text1,text2, m-1, n-1)
        print(memo)
        return res
    
    def longestCommonSubsequence_v2(self, text1: str, text2: str) -> int:
        m,n=len(text1), len(text2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j-1],dp[i-1][j], dp[i][j-1])
        return dp[m][n]


if __name__ == "__main__":
    solution = Solution()
    s1="bl"
    s2="yby"
    print(solution.longestCommonSubsequence_v2(s1,s2))