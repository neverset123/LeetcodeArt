#include "leetcode/binary_tree/TreeNode.h"  
#include <iostream>  
#include <vector>

class traverse {
public:
    std::vector<int> elements;
    void inorder(TreeNode* root) {
        if (root == NULL) return;
        inorder(root->left);
        elements.push_back(root->val);
        inorder(root->right);
    }
    void preorder(TreeNode* root) {
        if (root == NULL) return;
        elements.push_back(root->val);
        preorder(root->left);
        preorder(root->right);
    }
    void postorder(TreeNode* root) {
        if (root == NULL) return;
        postorder(root->left);
        postorder(root->right);
        elements.push_back(root->val);
    }
};

int main() {

    std::vector<int> levelOrder = {1, 2, 3, 4, 5, 6, 7};
    TreeNode* root = buildTree(levelOrder);
    traverse t;
    t.inorder(root);
    for (int i = 0; i < t.elements.size(); i++) {
        std::cout << t.elements[i] << " ";
    }
    std::cout << std::endl;
    t.elements.clear();
    t.preorder(root);
    for (int i = 0; i < t.elements.size(); i++) {
        std::cout << t.elements[i] << " ";
    }
    std::cout << std::endl;
    t.elements.clear();
    t.postorder(root);
    for (int i = 0; i < t.elements.size(); i++) {
        std::cout << t.elements[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}
