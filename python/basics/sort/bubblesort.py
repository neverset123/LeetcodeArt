# 时间复杂度: 最好O(n), 最坏O(n^2)
# 空间复杂度: O(1)

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr_test = [5,4,3,2,1]
    arr_sorted = bubblesort(arr_test)
    print(arr_sorted)