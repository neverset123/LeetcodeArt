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

    def level_traverse(self, root):
        if root == None:
            return []
        temp_list = []
        temp_list.append(root)
        self.elements.append(root.val)
        while(len(temp_list)!=0):
            self.level+=1
            print(f"level:{self.level}")
            size = len(temp_list)
            for i in range(size):
                ele = temp_list.pop()
                if ele.left != None:
                    temp_list.append(ele.left)
                    self.elements.append(ele.left.val)
                if ele.right != None:
                    temp_list.append(ele.right)
                    self.elements.append(ele.right.val)
        return self.elements


if __name__ == "__main__":
    test_data = [3,9,20,None,None,15,7]
    test_tree = from_list(test_data)
    print(Solution().level_traverse(test_tree))