class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def from_list(elements):
    if len(elements)==0:
        return None
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
        self.valid=True
        self.preNode=None

    def isValidBST(self, root):
        self.traverse(root)
        return self.valid
    
    def traverse(self, root):
        if root==None:
            return
        self.traverse(root.left)
        if self.preNode!=None and self.preNode.val>=root.val:
            self.valid=False
        self.preNode=root
        self.isValidBST(root.right)


if __name__ == "__main__":
    test_data = [10,5,15,None,None,6,20]
    test_tree = from_list(test_data)
    solution = Solution()
    print(solution.isValidBST(test_tree))