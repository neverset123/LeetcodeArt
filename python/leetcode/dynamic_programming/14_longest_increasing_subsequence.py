# 一维和二维最长递增子序列

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
        dp=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i], dp[j]+1)
        return max(dp)
    
    def Envelop_max(self, envelops):
        envelops.sort(key=lambda x: (x[0], -x[1]))
        temp_array=[ele[1] for ele in envelops]
        return self.lengthOfLIS(temp_array)
        

