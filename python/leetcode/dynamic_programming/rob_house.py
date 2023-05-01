from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        m=len(nums)
        memo=[-1]*m
        def dp(nums, index):
            if index>=m:
                return 0
            if memo[index]!=-1:
                return memo[index]
            memo[index]=max(dp(nums, index+1), dp(nums, index+2)+nums[index])
            return memo[index]
        return dp(nums, 0)

    def rob_v1(self, nums):
        m=len(nums)
        dp=[0]*m
        dp[m-1]=nums[m-1]
        dp[m-2]=max(nums[m-1], nums[m-2])
        for i in range(m-3, -1, -1):
            dp[i]=max(dp[i+1], dp[i+2]+nums[i])
        return dp[0]

    def rob_circle(self, nums):
        m=len(nums)
        if m==1:
            return nums[0]
        if m==2:
            return max(nums[0], nums[1])
        def rob_start_end(nums, start, end):
            memo=[-1]*(end-start+1)
            def dp(nums, start, end):
                if start>end:
                    return 0
                if start==end:
                    return nums[start]
                if memo[start]!=-1:
                    return memo[start]
                memo[start]=max(dp(nums, start+1, end), dp(nums, start+2, end)+nums[start])
                return memo[start]
            return dp(nums, start, end)
        return max(rob_start_end(nums, 0, m-2), rob_start_end(nums, 1, m-1))

    def rob_circle_v1(self, nums):
        m=len(nums)
        if m==1:
            return nums[0]
        if m==2:
            return max(nums[0], nums[1])
        def rob_start_end(nums, start, end):
            dp_i_1=0
            dp_i_2=0
            dp_i=0
            for i in range(end, start-1, -1):
                dp_i=max(dp_i_1, dp_i_2+nums[i])
                dp_i_2=dp_i_1
                dp_i_1=dp_i
            return dp_i
        return max(rob_start_end(nums, 0, m-2), rob_start_end(nums, 1, m-1))

    def rob_tree(self, root) -> int:
        if root==None:
            return 0
        if self.memo.get(root)!=None:
            return self.memo.get(root)
        rob_it = (root.val
                   +(0 if root.left==None else self.rob(root.left.left)+self.rob(root.left.right))
                   +(0 if root.right==None else self.rob(root.right.left)+self.rob(root.right.right))
                )
        rob_next= self.rob(root.left)+self.rob(root.right)
        res=max(rob_it, rob_next)
        self.memo[root]=res
        return res

if __name__ == "__main__":
    nums = [1]
    solution=Solution()
    print(solution.rob_circle_v1(nums))