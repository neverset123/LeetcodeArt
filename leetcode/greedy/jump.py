class Solution:
    def jump(self, nums):
        m=len(nums)
        max_dist=0
        for i in range(m-1):
            max_dist=max(max_dist, i+nums[i])
            if max_dist<=i:
                return False
        return max_dist>=m-1
    
    def jump_min_steps(self, nums):
        m=len(nums)
        end, max_dist, jumps=0, 0, 0
        for i in range(m-1):
            max_dist=max(max_dist, i+nums[i])
            if i==end:
                jumps+=1
                end=max_dist
        return jumps