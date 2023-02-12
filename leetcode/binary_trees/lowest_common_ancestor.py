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

def lca(root, val1, val2):
    if root==None:
        return
    if root.val==val1 or root.val==val2:
        return root
    left=lca(root.left, val1, val2)
    right=lca(root.right, val1, val2)
    if left!=None and right!=None:
        return root
    return left if left!=None else right

def lca_v1(root, node_list):
    if root==None:
        return
    vals_list=[node.val for node in node_list]
    if root.val in vals_list:
        return root
    left=lca_v1(root.left, node_list)
    right=lca_v1(root.right, node_list)
    if left!=None and right!=None:
        return root
    return left if left!=None else right

class Solution:
    def __init__(self):
        self.existence=[0,0]
    
    def lca_v2(self, root, p, q):
        node = self.find(root, p, q)
        if sum(self.existence)!=2:
            return 
        else: return node

    def find(self,root,p,q):
        if root==None:
            return
        left=self.find(root.left, p, q)
        right=self.find(root.right, p, q)
        if left!=None and right!=None:
            return root
        if root.val == p.val: 
            self.existence[0]=1
            return root
        if root.val==q.val: 
            self.existence[1]=1
            return root
        
        return left if left!=None else right

    def find_bst(self,root,min,max):
        if root==None:
            return
        if root.val<min:
            self.find_bst(root.left,min,max)
        if root.val>max:
            self.find_bst(root.right, min, max)
        return root
    
    def lca_bst(self, root, p, q):
        min_val=min(p.val,q.val)
        max_val=max(p.val, p.val)
        return self.find_bst(root, min_val, max_val)


if __name__ == "__main__":
    test_data = [5,3,6,2,4,None,None,1]
    test_tree = from_list(test_data)
    #test_node_list = [TreeNode(9), TreeNode(7)]
    #print(lca_v1(test_tree, test_node_list).val)
    solution=Solution()
    #node=solution.lca_v2(test_tree, TreeNode(9), TreeNode(7))
    node=solution.lca_bst(test_tree,TreeNode(6),TreeNode(1))
    print(node.val)