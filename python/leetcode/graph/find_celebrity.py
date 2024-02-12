# 可以利用排除法，先排除那些显然不是「名人」的人，从而避免 for 循环的嵌套，降低时间复杂度。
# 只要观察任意两个候选人的关系，一定能确定其中的一个人不是名人，把他排除

def knows(a, b):
    pass

def findCelebrity(self, n):
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate
