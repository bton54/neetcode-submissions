class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression to lead to almost O(1) finds
            return parent[x]

        
        def union(x1, x2):
            p1, p2 = find(x1), find(x2)

            # if same parent - already connected, return that we are NOT a valid tree
            # this is b/c a valid tree has NO cycles by definition


            if p1 == p2:
                return False

            # otherwise connect them

            # we don't really care too much about rank, but lets set it up for good practice
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]

            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        # need to check that all nodes are connected - 
        if len(edges) != n -1:
            return False
            
        parent = [i for i in range(n)] # no need to add +1 since we are 0 indexed
        rank = [1] * n 

        for u, v in edges:
            if not union(u,v): # on a fail, return false. if we make it all the way, return true

                return False

        return True

        # TC: O(E * V(* ackerman constant))
        # SC: O(N) for the extra space used by parent and rank arrays