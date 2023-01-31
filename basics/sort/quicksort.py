def quicksort(arr):
    if(len(arr)<=1):
        return arr
    else:
        pivot=arr[0]
        return (quicksort([element for element in arr if element <pivot])
                +[pivot]
                +quicksort([element for element in arr if element >pivot]))

if __name__ == "__main__":
    arr_test = [5,4,3,2,1]
    arr_sorted = quicksort(arr_test)
    print(arr_sorted)