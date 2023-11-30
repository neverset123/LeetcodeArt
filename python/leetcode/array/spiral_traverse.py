## 螺旋式遍历矩阵
def spiralTraverse(matrix):
    m = len(matrix)
    n = len(matrix[0])
    size = m*n
    left = 0
    right = n-1
    up = 0
    down = m-1
    result = []
    while(len(result)<size):
        # from left to right
        if(left<right):
            for i in range(left, right+1):
                result.append(matrix[up][i])
            up += 1
        # from up to down
        if(up<down):
            for i in range(up, down+1):
                result.append(matrix[i][right])
            right -= 1
        # from right to left
        if(left<right):
            for i in range(right, left-1, -1):
                result.append(matrix[down][i])
            down -= 1
        # from down to up
        if(up<down):
            for i in range(down, up-1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

if __name__ == "__main__":
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    print(spiralTraverse(matrix))