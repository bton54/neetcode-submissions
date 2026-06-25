class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # we can use the union find to check if these edges make a valid tree

        # we just need to look for a cycle (that would make this an invalid tree)

        # in union find, each node is it's own parent
        # it's 0 indexed, so we can set up a basic parent and also rank array
        parent = [i for i in range(n)]

        rank = [1] * n

        def find(x):
            # if we're not our own parent, recursively find the parent and return it
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x1,x2):
            # this is the merge function - we only merge if we have different parents and merge to the one of the higher rank.
            # then we add to the rank of the higher like we're playing yugioh

            p1, p2 = find(x1), find(x2)

            if p1 == p2: # we are the SAME parent already... then this is not a valid tree b/c there's a cycle
                return False

            else:
                # we can merge their parents
                if rank[p1] > rank[p2]: 
                    parent[p2] = p1 # specifically need to adjust the parent refernece pointers
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

            return True

        successful_unions = 0

        for x1, x2 in edges:
            if not union(x1, x2):
                return False
            else:
                successful_unions += 1
            
        return True if successful_unions == n-1 else False # we can form a valid tree if we have n-1 successful unions


            