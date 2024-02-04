#include <iostream>
#include <string>
#include "leetcode/binary_tree/TreeNode.h"

class deep_first_search
{
public:
    std::string path;
    std::string min_path;
    void shortest_path_from_leaf(TreeNode* root)
    {
        if (root == NULL) return;
        path.push_back('a' + root->val);
        if (root->left == NULL && root->right == NULL)
        {
            std::string temp = path;
            std::reverse(temp.begin(), temp.end());
            if (min_path == "" || temp < min_path) min_path = temp;
        }
        shortest_path_from_leaf(root->left);
        shortest_path_from_leaf(root->right);
        path.pop_back();
    }
};

int main()
{
    TreeNode* root = buildTree({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    deep_first_search dfs;
    dfs.shortest_path_from_leaf(root);
    std::cout << dfs.min_path << std::endl;
}



