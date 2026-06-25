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
    vector<int> rightSideView(TreeNode* root) {
        // we want to use a deque to process this in a bfs style

        if (root == nullptr) {
            return {};
        }

        vector<int> res;

        deque<TreeNode*> dq;

        dq.push_back(root);

        while(!dq.empty()) { // same as while(queue): 
            // we need to also do this for the number of nodes in the level
            // we need to call front and pop separately
            // node = q.popleft()

            int level = dq.size();

            for (int i = 0; i < level; i++) {
                TreeNode* node = dq.front();
                dq.pop_front();

                if (node->left != nullptr) {
                    dq.push_back(node->left);

                    // equivalent is if node.left: q.append(node.left)
                }

                if (node->right != nullptr) {
                    // if root.right:

                    dq.push_back(node->right);
                }

                if (i == level - 1) {
                    res.push_back(node->val);
                }
            }
        }
        return res;
    }
};
