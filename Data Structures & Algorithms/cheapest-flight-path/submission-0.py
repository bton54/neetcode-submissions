class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
            # we want to compute an edge list (not adj graph), storing src -> dst, weight
        # we also want to compute a table that shows the costs from getting from any source node to any destination.


        dist = [float('inf')] * n # cost from any source to dest is infinite to start.
        dist[src] = 0 # base case - we start at source, so it's free to get here.

        # we want to run Bellman Ford - relax the edges 1 at a time per iteration.
        # we need to make a copy 
        for _ in range(k+1): # we want to run k + 1 iterations 

            # make a copy to avoid using updated values in the same iteration
            # for example, if i update a cost in the iteration on a non copy, it might use the copy in calculations
            dist_copy = dist.copy()

            for u, v, cost in flights:
                # if we can reach u, lets try to update v's distance.

                if dist[u] != float('inf'):
                    # we want to compare to the previous iteration (non-copy)
                    dist_copy[v] = min(dist_copy[v] , dist[u] + cost)

            dist = dist_copy # update this for the next iteration

        # return the cost to reach dst in that number of stops if possible, otherwise -1
        return dist[dst] if dist[dst] != float('inf') else -1 

        # TC: O(V * E) where V is the number of nodes and E is the number of edges
            # It's actually k+1 iterations * E in this instance -> O(k * E)
        # SC: O(n) for the distance arrays