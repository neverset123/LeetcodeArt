#可以拓展为寻找左右边界
# 二分查找的时间复杂度是二叉树的高度log(N)

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
            right=mid-1
        elif arr[mid]>value:
            right=mid-1
        elif arr[mid]<value:
            left=mid+1
    if left>=len(arr) or arr[left]!=value:
        return -1
    return left



if __name__ == "__main__":
    arr_test = [1,2,3,4,5]
    print(left_boundary(arr_test,4))
       