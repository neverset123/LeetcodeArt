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
        self.elements = []
        self.de_elements = []

    def preorder_serialize(self, root):
        if root==None:
            self.elements.append("None")
            return "None"
        self.elements.append(str(root.val))
        self.preorder_serialize(root.left)
        self.preorder_serialize(root.right)
        return ",".join(self.elements)
    
    def preorder_deserialize(self, arr_str):
        self.de_elements = arr_str.split(",")
        ele=self.de_elements.pop(0)
        if ele=="None":
            return None
        root=TreeNode(ele)
        root.left=self.preorder_deserialize(",".join(self.de_elements))
        root.right=self.preorder_deserialize(",".join(self.de_elements))
        return root

if __name__ == "__main__":
    test_data = [1,2,None, 4,5]
    test_tree = from_list(test_data)
    solution = Solution()
    solution1=Solution()
    print(solution.preorder_serialize(test_tree))
    print(solution1.preorder_serialize(solution.preorder_deserialize(solution.preorder_serialize(test_tree))))
