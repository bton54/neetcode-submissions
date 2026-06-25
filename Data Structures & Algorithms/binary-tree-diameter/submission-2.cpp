/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        // we need to use a dfs
        // at step, we path the longest path upwards, but we can technically use the whole existing path in max calculations
        // this is to allow paths that DONT pass through the root

        int res = 0;
        dfs(root, res);
        return res;
    }

private:

    int dfs(TreeNode* root, int& res) {
        if (!root) {
            return 0;
        }

        // then we want to calculate the left and right path lengths

        int left = dfs(root->left, res);
        int right = dfs(root->right, res);

        res = max(res, left + right); // left + right b/c we can make the new root of the max diameter this tree
        return 1 + max(left, right); 
    }
};
