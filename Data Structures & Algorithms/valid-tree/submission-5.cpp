class Solution {


// we can use union find to see if this is a valid graph (acyclic graph)
// we can merge the edges
// if any of the merges is unsuccessful, we have a cycle (return false)
 
public:


    bool validTree(int n, vector<vector<int>>& edges) {
        // we need exactly n-1 edges for n nodes
        if (edges.size() != n-1) {
            return false;
        }

        // construct parent array

        vector<int> parent(n);

        for (int i = 0; i < n; ++i) {
            parent[i] = i; // everyone is their own parent to start
        }

        vector<int> rank(n, 1); // initialize a vector of size n with all values set to rank of 1

        // from here

        for (auto& edge : edges) {
            // since it's a vector, just access using indexing
            if (!(merge(edge[0] , edge[1], parent, rank))) {
                return false;
            }
        }

        return true;

        


    }

private:

    int find(int x1, vector<int>& parent) {
 
        if (x1 != parent[x1]) {
            // if they're not the parent, we need to find it using path compression
            parent[x1] = find(parent[x1], parent);
        }
        return parent[x1];
    }

    bool merge(int x1, int x2, vector<int>& parent, vector<int>& rank) {

        int p1 = find(x1, parent);
        int p2 = find(x2, parent);

        if (p1 == p2) {
            // then they're already merged
            return false;
        }

        // then we need to merge base don the rank

        int r1 = rank[p1];
        int r2 = rank[p2];

        if (r1 > r2) {
            // p1 dominates
            parent[p2] = p1;
            rank[p1] += r2;

        }
        else { 
            parent[p1] = p2;
            rank[p2] += r1;
        }
        return true;
    }
};
