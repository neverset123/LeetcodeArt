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
        print(root.val)
        self.preNode=root
        self.isValidBST(root.right)

    def search(self, root, target):
        if root==None:
            return
        if root.val==target:
            return root
        elif root.val>target:
            return self.search(root.left, target)
        else:
            return self.search(root.right, target)

    def insert(self, root, val):
        if root==None:
            return TreeNode(val)
        if root.val>val:
            root.left=self.insert(root.left, val)
        elif root.val<val:
            root.right=self.insert(root.right, val)
        return root

    def delete(self, root, val):
        if root==None:
            return
        if root.val==val:
            if root.left==None:
                return root.right
            if root.right==None:
                return root.left
            else:
                node_next=self.min(root.right)
                root.right=self.delete(root.right, node_next.val)
                #root.val=node_next.val
                node_next.left=root.left
                node_next.right=root.right
                root=node_next
        elif root.val>val:
            root.left=self.delete(root.left, val)
        else:
            root.right=self.delete(root.right, val)
        return root
    
    def min(self, root):
        if root==None:
            return
        return root if root.left == None else self.min(root.left)

if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    test_tree = from_list(test_data)
    solution = Solution()
    #solution.traverse(test_tree)
    solution.delete(test_tree, 2)
    solution.traverse(test_tree)