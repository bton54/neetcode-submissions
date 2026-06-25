"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # we want to create a mapping from the old to new map

        old_to_new = {}

        if not node:
            return None

        def dfs(node):

            # we get the 1st node in the graph 
            # each node has a val and neighbors

            # lets create the node. if it already exists, we can just return that mapping
            if node in old_to_new:
                return old_to_new[node]

            # otherwise, we create a new node
            new_node = Node(node.val)

            # now map this old node to the new one in the graph
            old_to_new[node] = new_node

            # now we want to recursively call this clone function on the neighbors
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            
            return new_node

        return dfs(node)

        # TC: O(V + E)
        # SC: O(V)
            

        