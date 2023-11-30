# rorate a matrix 90 degree
# 可以分为两步: 沿对角线镜像和沿竖轴翻转

def rotate(matrix):
    m=len(matrix)
    matrix = mirror(matrix)
    for i in range(m):
        matrix[i] = reverse(matrix[i])
    return matrix

def mirror(matrix):
    m=len(matrix)
    for i in range(m):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def reverse(row):
    n = len(row)
    for j in range(n//2):
        row[j], row[n-1-j] = row[n-1-j], row[j]
    return row


if __name__ == "__main__":
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]
    print(rotate(matrix))