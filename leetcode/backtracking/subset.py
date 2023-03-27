class Solution:
    def canPartitionKSubsets(self, nums, k):
        if k==0:
            return True
        m=len(nums)
        if k>m:
            return False
        sum_all=sum(nums)
        if sum_all%k!=0:
            return False
        used=[False]*m
        target=sum_all//k
        def backtrack(k, bucket, nums, start):
            if bucket==target:
                return backtrack(k-1, 0, nums, 0)
            for i in range(start, m):
                if used[i]==True:
                    continue
                if bucket+nums[i]>target:
                    continue
                used[i]=True
                if backtrack(k, bucket+nums[i], nums, i+1):
                    return True
                used[i]=False
            return False
        return backtrack(k, 0, nums, 0)