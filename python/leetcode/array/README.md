## tips
1. slicing an array with index out of range will not result error (eg. [1,2,3][3:] returns only empty array)
2. if element in list is dictionary or list, it is mutable. if you need append an object to list that is not changable, use copied object

## create array
1. #2d array
[[0]*n for _ in range(n)]
不要用[[0]*len(s1)]*len(s2)!!

## array properties
#sort array
sorted(array)
array.sort(key=lambda x: ...)
array.remove(ele)
#find index of ele
array.index(ele)

