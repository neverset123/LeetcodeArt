#快速排序就是构造二叉搜索树的过程，是二叉树的前序遍历
#时间复杂度是整棵树中数组元素的个数，
#二叉树每一层元素数是N，分界点均匀的情况下，树的深度为logN，所以理想情况下总复杂度为NlogN
#理想情况下空间复杂度为递归堆栈的深度logN
#是不稳定性排序(相同元素的相对位置可能发生变化)
def quicksort_v1(arr):
    if len(arr)<=1:
        return arr
    arr_left=[]
    pivot=arr[0]
    arr_right=[]
    for ele in arr[1:]:
        if ele<pivot:
            arr_left.append(ele)
        else:
            arr_right.append(ele)
    arr_left_sorted=quicksort(arr_left)
    arr_right_sorted=quicksort(arr_right)
    return arr_left_sorted+[pivot]+arr_right_sorted

def swap(arr, i, j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

#partition list with pivot
def partition(arr, left, right):
    pivot=left
    while(left<right):
        while(left<right and arr[pivot]>arr[left+1]):
            left+=1
        while(left<right and arr[pivot]<=arr[right]):
            right-=1
        swap(arr, left, right)
    swap(arr, pivot, right)
    return right

def quicksort_v2(arr, left, right):
    if left>=right:
        return arr
    pivot=partition(arr, left, right)
    quicksort_v2(arr, left, pivot-1)
    quicksort_v2(arr, pivot+1, right)
    return arr
        
def quicksort(arr):
    if(len(arr)<=1):
        return arr
    else:
        pivot=arr[0]
        return (quicksort([element for element in arr[1:] if element <pivot])
                +[pivot]
                +quicksort([element for element in arr[1:] if element >=pivot]))

def find_kthlargest(arr, k):
    if k>len(arr):
        return -1
    n=len(arr)
    left=0
    right=n-1
    while(left<=right):
        pivot=partition(arr, left, right)
        if pivot>n-k:
            right=pivot-1
        elif pivot<n-k:
            left=pivot+1
        else:
            return arr[pivot]
    return -1

if __name__ == "__main__":
    arr_test = [5,4,4,3,3,2,1]
    #arr_sorted = quicksort_v1(arr_test)
    #arr_sorted = quicksort_v2(arr_test, 0, len(arr_test)-1)
    #print(arr_sorted)
    #print(partition(arr_test, 0, 4))
    print(find_kthlargest(arr_test, 3))