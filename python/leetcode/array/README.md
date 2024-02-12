## tips
1. slicing an array with index out of range will not result error (eg. [1,2,3][3:] returns only empty array)
2. if element in list is dictionary or list, it is mutable. if you need append an object to list that is not changable, use copied object

## create array
1. 2d array
[[0]*n for _ in range(n)]
不要用[[0]*len(s1)]*len(s2)!!
2. 3d array
[[[0, 0] for _ in range(m)] for _ in range(m)]
3. 最大正整数是 sys.maxsize; 最小负整数是-sys.maxsize-1

## add/remove last element
array.append(ele) # append is adding a reference to the ele, if no mutable is expected, a deep copy is neeeded
array.pop()

## add/remove at specific position
array.insert(pos, ele)
array.pop(pos)

## array properties
#sort array
sorted(array) # it returns new sorted list, the original sequence remains unchanged. It can be used with any iterable
array.sort(key=lambda x: ...) # sort element in place
array.remove(ele)
#find index of ele
array.index(ele)

## list copy
```
#shallow copy
[1,2,3].copy()
```
## list concatenate
```
[1,2,3] +[1]
```

