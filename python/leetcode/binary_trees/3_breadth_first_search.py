# 广度优先，一般用于求最短路径
# 层序遍历，迭代算法

from utils import TreeNode, from_list
from typing import List

class Solution:
    def __init__(self):
        self.elements = []
        self.level=0

    def minDepth(self, root):
        if root==None:
            return 0
        depth=0
        temp_list=[root]
        while(len(temp_list)!=0):
            size=len(temp_list)
            depth+=1
            for i in range(size):
                ele = temp_list.pop(0)
                if ele.left==None and ele.right==None:
                    return depth
                if ele.left!=None:
                    temp_list.append(ele.left)
                if ele.right!=None:
                    temp_list.append(ele.right)

    def plus_one(self, ele, index):
        if ele[index]=="9":
            return ele[:index]+"0"+ele[index+1:]
        else:
            return ele[:index]+chr(ord(ele[index])+1)+ele[index+1:]

    def minus_one(self, ele, index):
        if ele[index]=="0":
            return ele[:index]+"9"+ele[index+1:]
        else:
            return ele[:index]+chr(ord(ele[index])-1)+ele[index+1:]

    def openLock(self, deadends: List[str], target: str) -> int:
        temp_list= ["0000"]
        steps=0
        used=[]
        while(len(temp_list)!=0):
            size=len(temp_list)
            for i in range(size):
                ele=temp_list.pop(0)
                if ele==target:
                    return steps
                if ele in deadends:
                    continue
                for j in range(len(ele)):
                    new_eles=[self.plus_one(ele, j),self.minus_one(ele, j)]
                    for new_ele in new_eles:
                        if new_ele not in used:
                            used.append(new_ele)
                            temp_list.append(new_ele)
            steps+=1
        return -1

    def level_traverse_largest_value(self, root):
        if root == None:
            return
        temp_list = []
        max_list = []
        temp_list.append(root)
        while(len(temp_list)!=0): #负责从上到下
            max_list.append(max([ele.val for ele in temp_list]))
            size = len(temp_list)
            for i in range(size): #负责从左到右
                ele = temp_list.pop(0)
                if ele.left != None:
                    temp_list.append(ele.left)
                if ele.right != None:
                    temp_list.append(ele.right)
        return max_list
    
    # find min steps from start to goal in grid with obstacles
    def cal_cell_value(self, grid, start, goal, cost):
        import sys
        delta = [[-1, 0 ], # go up
            [ 0, -1], # go left
            [ 1, 0 ], # go down
            [ 0, 1 ]] # go right
        if goal == start:
            return 0
        if grid[start[0]][start[1]] == 1:
            return 99
        m=len(grid)
        n=len(grid[0])
        cost_table = [[sys.maxsize]*n for _ in range(m)]
        cost_table[start[0]][start[1]] = 0
        temp_list = [start]
        while(len(temp_list)!=0):
            size = len(temp_list)
            for i in range(size):
                ele = temp_list.pop()
                if ele == goal:
                    return cost_table[goal[0]][goal[1]]
                for opt in delta:
                    if ele[0]+opt[0]>=0 and ele[0]+opt[0] <m and ele[1]+opt[1]>=0 and ele[1]+opt[1]<n and grid[ele[0]+opt[0]][ele[1]+opt[1]] !=1 and cost_table[ele[0]+opt[0]][ele[1]+opt[1]] ==sys.maxsize:
                        cost_table[ele[0]+opt[0]][ele[1]+opt[1]] = cost_table[ele[0]][ele[1]] + cost
                        temp_list.append([ele[0]+opt[0], ele[1]+opt[1]])
        return cost_table[goal[0]][goal[1]]
    
    def compute_value(self, grid,goal,cost):
        value = [[self.cal_cell_value(grid, [row, col], goal, cost) for col in range(len(grid[0]))] for row in range(len(grid))]
        return value 

if __name__ == "__main__":
    # test_data = [1,3,2,5,3,None,9]
    # test_tree = from_list(test_data)
    # print(Solution().level_traverse_largest_value(test_tree))
    dead_locks=["5557","5553","5575","5535","5755","5355","7555","3555","6655","6455","4655","4455","5665","5445","5645","5465","5566","5544","5564","5546","6565","4545","6545","4565","5656","5454","5654","5456","6556","4554","4556","6554"]
    target="5555"
    print(Solution().openLock(dead_locks, target))
