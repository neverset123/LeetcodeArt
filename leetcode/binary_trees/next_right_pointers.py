from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node

class Solution:
    def __init__(self):
        self.elements = []
        self.level=0

    def connect_v1(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        if root==None:
            return 
        temp_list = []
        temp_list.append(root)
        while(len(temp_list)!=0):
            size=len(temp_list)
            for i in range(size):
                ele = temp_list.pop(0)
                if i!=size-1:
                    ele.next=temp_list[0]
                if ele.left!=None:
                    temp_list.append(ele.left)
                if ele.right !=None:
                    temp_list.append(ele.right)
        return root
    
    #模拟三叉树遍历
    def connect(self, root):
        if root==None:
            return 
        self.traverse(root.left, root.right)
        return root
    
    def traverse(self, node1, node2):
        if node1==None or node2==None:
            return
        node1.next=node2
        self.traverse(node1.left, node1.right)
        self.traverse(node2.left, node2.right)
        self.traverse(node1.right, node2.left)

if __name__ == "__main__":
    test_data = [1,3,2,5,3,None,9]
    test_tree = from_list(test_data)
    print(Solution().connect(test_tree))