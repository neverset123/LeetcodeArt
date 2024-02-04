#include <iostream>
#include <string>
#include "leetcode/binary_tree/TreeNode.h"

class breadth_first_search {
public:
    std::string path;
    int min_depth(TreeNode* root)
    {
        if(root==NULL) return 0;
        std::queue<TreeNode*> q;
        q.push(root);
        int depth = 1;
        while(q.empty()==false)
        {
            int size = q.size();
            for(int i=0; i<size; i++)
            {
                TreeNode* node = q.front();
                q.pop();
                if(node->left==NULL && node->right==NULL) return depth;
                if(node->left!=NULL) q.push(node->left);
                if(node->right!=NULL) q.push(node->right);
            }
            depth++;
        }
    }
};

int main()
{
    TreeNode* root = buildTree({1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
    breadth_first_search bfs;
    std::cout << bfs.min_depth(root) << std::endl;
}