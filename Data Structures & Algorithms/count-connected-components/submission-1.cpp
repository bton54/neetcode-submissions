class Solution {

public:

    int find(int x, vector<int>& parent) {
        // if we aren't our own parent, recursively find 

        if (x != parent[x]) {
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }

    bool union_elements(int x1, int x2, vector<int>& parent, vector<int>& rank) {

        // if the parents are the same, return early
        // we can do false for failed union

        int parent1 = find(x1, parent);
        int parent2 = find(x2, parent);

        if (parent1 == parent2) {
            return false;
        }

        // otherwise, get the ranks

        int rank1 = rank[parent1];
        int rank2 = rank[parent2];

        // then we can compare the rank and adjust the parents

        if (rank1 > rank2) {
            // then we can adjust the parent and increment the rank
            rank[parent1] += rank2;
            parent[parent2] = parent1;
        }

        else {
            rank[parent2] += rank1;
            parent[parent1] = parent2;
        }

        return true;
    }

    int countComponents(int n, vector<vector<int>>& edges) {

        // we want to define a parent array for the number of nodes
        // every node is its own parent and we have rank of 1

        vector<int> rank(n, 1);
        vector<int> parent(n);

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        // 

        // then we want to iterate through the list of edges and then try to merge them

        // start with n, then decrement for each successful merge

        int res = n;

        for (auto& edge : edges) {
            int a = edge[0];
            int b = edge[1];
            if (union_elements(a, b, parent, rank)) {
                res--;
            }
        }

        return res;

    }
};


// we have to define a parent and rank array
// we can find and merge, use path compression to get an amortized almost constant time (inverse ack man) 

