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
    int res = INT_MIN;
    int maxPathSum(TreeNode* root) {
        // maximum path sum. we basically want to get the maximum  possible path through the true
        // we don't have to start at the root, so this means we can run a maximum path comparison inclusive of the root when exploring with a dfs
        // however, we return up the greater of the left or right path though.
        // this is b/c we have to respect the previous path being the root

        if (root == nullptr) {
            // return; // this is edge case
            return 0;
        }
        dfs(root);
        return res;

        
    }

    // integer return type 
    int dfs(TreeNode* node) {
        //

        if (node == nullptr) {
            return 0; // we return 0 if its null
        }

        // now we need the values of the left and right trees

        int leftSum = max(dfs(node->left) , 0); // we want to compare against 0 b/c we don't want to consider negative paths
        int rightSum = max(dfs(node->right) , 0);

        // now we want to update the path sum
        res = max(res, leftSum + node->val + rightSum);

        // then we want to return up the greater of the path
        return node->val + max(leftSum, rightSum);
    }
};
