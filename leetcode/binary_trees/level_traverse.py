from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

    def level_traverse_largest_value(self, root):
        if root == None:
            return
        temp_list = []
        max_list = []
        temp_list.append(root)
        while(len(temp_list)!=0):
            max_list.append(max([ele.val for ele in temp_list]))
            size = len(temp_list)
            for i in range(size):
                ele = temp_list.pop(0)
                if ele.left != None:
                    temp_list.append(ele.left)
                if ele.right != None:
                    temp_list.append(ele.right)
        return max_list

if __name__ == "__main__":
    test_data = [1,3,2,5,3,None,9]
    test_tree = from_list(test_data)
    print(Solution().level_traverse_largest_value(test_tree))
    print([[1,2,3], [4,5], [3,9]][::-1])