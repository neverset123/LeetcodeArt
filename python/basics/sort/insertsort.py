def insertsort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

if __name__ == "__main__":
    arr_test = [5,4,3,2,1]
    arr_sorted = insertsort(arr_test)
    print(arr_sorted)
       