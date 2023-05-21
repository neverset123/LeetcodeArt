#测试没通过，不知道为啥
# 博弈问题

from typing import List

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        m=len(nums)
        # dp[i][j]=[first, second]分别表示在石堆[i,j]中
        # 先手、后手能获得的最高得分
        dp=[[[0, 0]]*m for _ in range(m)]
        for i in range(m):
            dp[i][i]=(nums[i], 0)
        for i in range(m-2, -1, -1):
            for j in range(i+1, m):
                # 选择左边
                left=nums[i]+dp[i+1][j][1]
                # 选择右边
                right=nums[j]+dp[i][j-1][1]
                if left>right:
                    dp[i][j][0]=left
                    dp[i][j][1]=dp[i+1][j][0]
                else:
                    dp[i][j][0]=right
                    dp[i][j][1]=dp[i][j-1][0]

        return True if dp[0][m-1][0]-dp[0][m-1][1]>=0 else False
                
if __name__ == "__main__":
    nums=[2,4,55,6,8]
    solution = Solution()
    print(solution.PredictTheWinner(nums))
