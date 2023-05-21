# 找到和最大的子数组， dp[i]是以nums[i]结尾的最大子数组和
# 以nums[i]为结尾的「最大子数组和」为dp[i]

import sys
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[-sys.maxsize - 1]*len(nums)
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i], dp[i-1]+nums[i])
        # 遍历所有的子数组和
        res = max(dp)
        return res