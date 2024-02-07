#可以拓展为寻找左右边界
# 二分查找的时间复杂度是二叉树的高度log(N)
# 在for循环中的单调函数都可以有优化为二分查找
# 如果题目要求对数的复杂度O(NlogN)，一般都要往二分查找的方向上靠
# 二分查找就是在数组中实现的二叉搜索树查找的过程

def binarysearch(arr,value):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=left+(right-left)//2
        if arr[mid]==value:
            return mid
        elif arr[mid]<value:
            left=mid+1
        elif arr[mid]>value:
            right=mid-1
    return -1

def left_boundary(arr,value):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid=left+(right-left)//2
        if arr[mid]==value:
            right=mid-1     #寻找左边界，如果找到了，继续往左找
        elif arr[mid]>value:
            right=mid-1
        elif arr[mid]<value:
            left=mid+1
    if left>=len(arr) or arr[left]!=value:
        return -1
    return left

# KOKO吃香蕉
def min_eating_speed(piles, H):
    left = 1
    right = max(piles)
    while(left <= right):
        mid = left + (right - left) // 2
        if can_finish(piles, mid, H):
            right = mid-1
        else:
            left = mid + 1
    return left

def can_finish(piles, speed, H):
    time = 0
    for n in piles:
        time += n // speed + (1 if n % speed > 0 else 0)
    return time <= H

# 运送包裹的船
def ship_within_days(weights, D):
    left = max(weights)
    right = sum(weights)
    while(left <= right):
        mid = left + (right-left)//2
        if can_ship(weights, mid, D):
            right = mid-1
        else:
            left = mid+1
    return left

def can_ship(weights, capacity, D):
    days = 1
    cur_weight = 0
    for w in weights:
        cur_weight += w
        if cur_weight > capacity:
            days += 1
            cur_weight = w
    return days <= D

# 分割数组的最大值
def split_array(nums, m):
    left = max(nums)
    right = sum(nums)
    for i in range(left, right+1):
        n = can_split(nums, i)
        if(n <= m):
            return i
    return -1

def can_split(nums, max_sum):
    count = 1
    cur_sum = 0
    for n in nums:
        cur_sum += n
        if cur_sum > max_sum:
            count += 1
            cur_sum = n
    return count

if __name__ == "__main__":
    # arr_test = [1,2,3,4,5]
    # print(left_boundary(arr_test,4))
    # piles = [30,11,23,4,20]
    # H = 5
    # print(min_eating_speed(piles,H))
    # weights = [1,2,3,4,5,6,7,8,9,10]
    # D = 5
    # print(ship_within_days(weights,D))
    nums = [7,2,5,10,8]
    m = 2
    print(split_array(nums, m))
       