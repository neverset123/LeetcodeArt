import sys
from types import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-sys.maxsize - 1]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i], dp[i-1]+nums[i])
        res=dp[0]
        for i in range(len(nums)):
            res=max(res, dp[i])
        return res