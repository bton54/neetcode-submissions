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
    int kthSmallest(TreeNode* root, int k) {
        // a inorder traversal for a BST gives a sorted order  
        // use DFS
        vector<int> arr;
        dfs(root, arr);

        return arr[k-1]; // k-1 b/c it's 0 indexing. but kth is 1 indexing 2nd 3rd

    }
    void dfs(TreeNode* root, vector<int>& arr) {
        // we check for non root
        if (root == nullptr) {
            return;
        }

        dfs(root->left, arr);
        // then we actually want to add the value 
        arr.push_back(root->val);
        dfs(root->right, arr);
    }
};
