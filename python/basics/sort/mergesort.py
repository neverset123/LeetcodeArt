# 算法复杂度就是子问题的个数*子问题的复杂度，
# 子问题个数就是二叉树节点数N，子问题的复杂度就是每个节点子数组的长度，
# 所以总的复杂度就是二叉树中所有数组元素的个数
# 也就是树的深度*每一层元素的个数=NlogN
# 是稳定排序，相同元素的相对位置不发生变化
# 归并排序时二叉树的后序遍历
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