/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    vector<int> rightSideView(TreeNode *root) {
        vector<int> ret;
        queue<TreeNode *> que;
        if (root) {
            unsigned int leaf_num = 0, remain_leaf = 1;
            que.push(root); 

            while (!que.empty()) {
                TreeNode *node = que.front();
                que.pop();
                if (node->left) {
                    ++leaf_num;
                    que.push(node->left);
                }
                if (node->right) {
                    ++leaf_num;
                    que.push(node->right);
                }
                if (--remain_leaf == 0) {
                    ret.push_back(node->val);
                    remain_leaf = leaf_num;
                    leaf_num = 0;
                }
            }
        }
        return ret;
    }
};
