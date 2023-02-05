import copy

class Solution:
    def mergesort(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        left=self.mergesort(nums[:mid])
        right=self.mergesort(nums[mid:])
        return self.merge(left, right)

    def merge(self, nums1, nums2):
        results = []
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                results.append(nums1[i])
                i+=1
            else:
                results.append(nums2[j])
                j+=1
        results+=nums1[i:]
        results+=nums2[j:]
        return results

if __name__ == "__main__":
    arr_test = [5,4,3,2,1]
    solution = Solution()
    arr_sorted = solution.mergesort(arr_test)
    print(arr_sorted)