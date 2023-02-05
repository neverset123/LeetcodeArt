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
        self.current_rank = 0
        self.rank_val = None

    def in_traverse(self, root, rank):
        if root==None:
            return
        self.in_traverse(root.left, rank)
        self.current_rank+=1
        if self.current_rank==rank:
            self.rank_val = root.val
            return
        self.in_traverse(root.right, rank)
    
if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    rank = 3
    test_tree = from_list(test_data)
    solution = Solution()
    solution.in_traverse(test_tree, rank)
    print(solution.rank_val)