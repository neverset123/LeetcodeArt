from utils import TreeNode, from_list

class Solution:
    def __init__(self):
        self.nodes_str = ""

    def preorder_serialize(self, root):
        if root==None:
            self.nodes_str+="None,"
            return "None" # if tree is empty return "None"
        self.nodes_str+=(str(root.val)+",")
        self.preorder_serialize(root.left)
        self.preorder_serialize(root.right)
        return self.nodes_str[:-1]
    
    def preorder_deserialize(self, arr_str):
        try:
            index = arr_str.index(",")
            self.nodes_str=arr_str[index+1:]
        except ValueError:
            if arr_str!="None":
                return TreeNode(arr_str)
            return None
        ele=arr_str[:index]
        if ele=="None":
            return None
        root=TreeNode(ele)
        root.left=self.preorder_deserialize(self.nodes_str)
        root.right=self.preorder_deserialize(self.nodes_str)
        return root

if __name__ == "__main__":
    test_data = [1,2,3,None,None,4,5]
    test_tree = from_list(test_data)
    solution = Solution()
    solution1=Solution()
    # print(solution.preorder_serialize(test_tree))
    print(solution1.preorder_serialize(solution.preorder_deserialize(solution.preorder_serialize(test_tree))))
