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

if __name__ == "__main__":
    arr_test = [1,2,3,4,5]
    print(binarysearch(arr_test,4))
       