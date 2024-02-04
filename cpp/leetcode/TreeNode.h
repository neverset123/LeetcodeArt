#include <iostream>
#include <queue>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* buildTree(std::vector<int> levelOrder) {
    if (levelOrder.empty()) return NULL;

    std::queue<TreeNode*> q;
    TreeNode* root = new TreeNode(levelOrder[0]);
    q.push(root);

    for (int i = 1; i < levelOrder.size(); i += 2) {
        TreeNode* parent = q.front();
        q.pop();

        if (levelOrder[i] != -1) {  // Assuming -1 represents a null node
            parent->left = new TreeNode(levelOrder[i]);
            q.push(parent->left);
        }

        if (i + 1 < levelOrder.size() && levelOrder[i + 1] != -1) {
            parent->right = new TreeNode(levelOrder[i + 1]);
            q.push(parent->right);
        }
    }

    return root;
}