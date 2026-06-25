# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BST's basically mean that the root is > left and < right for all nodes in the tree
        # we can start off with a recursive function to explore the tree

        if not root:
            return True # edge case - empty tree is a valid BST

        def validate_bst(root, left, right):
            if not root:
                return True # if we went out of bounds, this is correct - we have a full BST

            # we need to make sure that the root is > left and < right
            if root.val <= left or root.val >= right:
                return False

            # then we need to recursively validate that this holds tree both children
            # the core with using infinity is b/c we need to reuse the previous values for boundaries
                # prevents cases of going right from root (ex. 5->7) and then left from new node (ex. 7 -> 4)
                # 4 is placed in a place that is supposed to be > than root.

            
            return validate_bst(root.left, left, root.val) and validate_bst(root.right, root.val, right)

        return validate_bst(root,  float('-inf'), float('inf'))
            