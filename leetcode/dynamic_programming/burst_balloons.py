class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        m=len(nums)
        temp_nums=[1]+nums+[1]
        dp=[[0]*(m+2) for _ in range(m+2)]
        for i in range(m+1, -1, -1):
            for j in range(i+1, m+2):
                for k in range(i+1, j):
                    dp[i][j]=max(dp[i][j], dp[i][k]+dp[k][j]+temp_nums[i]*temp_nums[k]*temp_nums[j])
        return dp[0][m+1]
