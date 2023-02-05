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
        self.subtree=dict()
        self.duplicate_subtree_list = []

    def postorder_serialize(self, root):
        if root==None:
            return "None"
        left=self.postorder_serialize(root.left)
        right=self.postorder_serialize(root.right)
        elements_str = left+","+right+","+str(root.val)
        if elements_str in self.subtree:
            self.subtree[elements_str]+=1
            if self.subtree[elements_str]==2:
                self.duplicate_subtree_list.append(root)
        else: self.subtree[elements_str]=1
        return elements_str

    def find_duplicates(self, root):
        self.postorder_serialize(root)
        return self.duplicate_subtree_list


if __name__ == "__main__":
    test_data = [1,2,3,4,None,2,4,None,None,4]
    test_tree = from_list(test_data)
    solution = Solution()
    print([item.val for item in solution.find_duplicates(test_tree)])
