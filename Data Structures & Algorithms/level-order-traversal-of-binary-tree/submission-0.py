# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        # traverse thru the true using bfs to get layer / level order traversal

        queue = collections.deque([root])

        res = []

        while queue:
            level_length = len(queue)

            level = []

            # add all the nodes on the same level 
            for i in range(level_length):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                res.append(level)

        return res

        


           


        