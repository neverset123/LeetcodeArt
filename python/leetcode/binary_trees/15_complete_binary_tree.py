#子问题复杂度是while循环logN，子问题个数为树的高度logN，所以总复杂度为logN*logN
#完全二叉树的每一层都是紧凑靠左排列的
#该题为计算完全二叉树的节点数
#完全二叉树的题与层序遍历关联

from utils import TreeNode, from_list

class Solution:
    def countNodeCompleteTree(self,root):
        if root==None:
            return 0
        leftTree=root.left
        rightTree=root.right
        h_left=1
        h_right=1
        #计算树的高度
        while(leftTree!=None):
            leftTree=leftTree.left
            h_left+=1
        while(rightTree!=None):
            rightTree=rightTree.right
            h_right+=1
        #分满二叉树和普通二叉树进行计算
        if h_left==h_right:
            return int(2**h_left)-1
        else:
            return 1+self.countNodeCompleteTree(root.left)+self.countNodeCompleteTree(root.right)

    def isCompleteTree(self, root: 'TreeNode') -> 'bool':
        i, bfs = 0, [root]
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])

if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    test_tree = from_list(test_data)
    solution=Solution()
    print(solution.countNodeCompleteTree(test_tree))
