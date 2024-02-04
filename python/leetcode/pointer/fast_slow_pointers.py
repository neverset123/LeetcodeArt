# 链表字串问题适合用快慢指针解决

class Solution:
    # remove duplicates from sorted array and return length
    def remove_duplicate(self, nums):
        if len(nums)<=1:
            return len(nums)
        slow= 0
        fast= 0
        for i in range(len(nums)):
            if nums[slow]!=nums[fast]:
                slow+=1
                nums[slow]=nums[fast]
            fast+=1
        return slow+1

    # remove values from list and return length
    def remove_values(self, nums, val):
        if len(nums)==0:
            return 0
        slow=0
        fast=0
        for i in range(len(nums)):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

    # move zeros to end of list
    def move_zeros(self, nums):
        if len(nums)==0:
            return
        slow=0
        fast=0
        for i in range(len(nums)):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                nums[fast]=0
                slow+=1
            fast+=1
        return slow
    
if __name__ == "__main__":
    test_data = [0,0,1,1,2,2,3]
    solution = Solution()
    # print(test_data[:solution.remove_duplicate(test_data)])
    # print(test_data[:solution.remove_values(test_data, 1)])
    solution.move_zeros(test_data)
    print(test_data)
