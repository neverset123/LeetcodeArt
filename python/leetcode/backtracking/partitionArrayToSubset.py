#判断array能否分成k等份

class Solution:

    #回溯解法，array角度
    def canPartitionKSubsets(self, nums, k):
        size = len(nums)
        if k>size: return False
        sum_nums=sum(nums)
        if sum_nums%k!=0: return False
        bucket_arr = [0]*k
        target = sum_nums//k
        return self.backtrack(nums, 0, bucket_arr, target)

    def backtrack(self, nums, index, bucket_arr, target):
        #判断回溯结束条件
        if index==len(nums):
            if all([bucket==target for bucket in bucket_arr]):
                return True
            else: return False
        # nums中每个元素可以选择装入哪个桶
        for bucket_id in range(len(bucket_arr)):
            #剪枝:每个bucket不超过target
            if bucket_arr[bucket_id]+nums[index]>target:
                continue
            bucket_arr[bucket_id]+=nums[index]
            # 一旦找到一组结果，就结束递归
            if self.backtrack(nums, index+1, bucket_arr, target):
                return True
            bucket_arr[bucket_id]-=nums[index]
        return False

    #回溯解法，bucket角度
    def canPartitionKSubsets_v1(self, nums, k):
        size = len(nums)
        if size<k: return False
        sum_nums=sum(nums)
        if sum_nums%k!=0: return False
        target = sum_nums//k
        used=[False]*size
        return self.backtrack_v1(k, 0, nums, 0, target, used)
    
    def backtrack_v1(self, k, bucket, nums, index, target, used):
        #所有桶都装满了
        if k == 0:
            return True
        #当前桶装满了
        if bucket == target:
            return self.backtrack_v1(k-1, 0, nums, 0, target, used)
        
        for id in range(index, len(nums)):
            if used[id]:
                continue
            if nums[id]+bucket>target:
                continue
            used[id] = True
            bucket+=nums[id]
            #提前结束递归
            if self.backtrack_v1(k, bucket, nums,  id+1, target, used):
                return True
            bucket-=nums[id]
            used[id]=False
        return False



    # 用贪心算法求解
    def canPartitionKSubsets_v2(self, nums, k):
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
        #以桶的视角遍历,需装满k个空桶
        def backtrack(k, bucket, nums, start):
            #还剩k-1个桶待装
            if bucket==target:
                return backtrack(k-1, 0, nums, 0)
            for i in range(start, m):
                if used[i]==True:
                    continue
                if bucket+nums[i]>target:
                    continue
                #做选择
                used[i]=True
                # 剩余数字可以装满当前桶
                if backtrack(k, bucket+nums[i], nums, i+1):
                    return True
                #撤销选择
                used[i]=False
            return False
        return backtrack(k, 0, nums, 0)

if __name__ == "__main__":
    nums = [4,3,2,3,5,2,1]
    k = 4
    print(Solution().canPartitionKSubsets_v1(nums, k))