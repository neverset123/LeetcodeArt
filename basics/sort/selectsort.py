def selectsort(arr):
    arr_sorted=[]
    for i in range(len(arr)):
        arr_sorted.append(min(arr[i:]))
    return arr_sorted

if __name__ == "__main__":
    arr_test = [5,4,3,2,1]
    arr_sorted = selectsort(arr_test)
    print(arr_sorted)