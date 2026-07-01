class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // we want to use a topological sort to solve this question
        // map all of the prereqs in an adj list
        // count indegree using array
        // use queue to execute bfs to check if all classes are reachable.

        // we can count the number of course we take each pop can compare to numCourses in the end

        unordered_map<int, vector<int>> adj; // this is the adjacency list
        vector<int> indegree(numCourses, 0); // indegree list - there's num # of nodes + all value start at 0

        // build the adj graph

        for (auto& pre : prerequisites) { 
            // we need to map b -> a b/c you need to take b before a
            // increase a's indegree b/c it has an extra depednency

            adj[pre[1]].push_back(pre[0]);
            indegree[pre[0]]++;
        }

        // we want to build the queue for the BFS

        queue<int> q;

        for (int i = 0; i < numCourses; ++i) {
            // if the indegree is 0 we can add it
            if (indegree[i] == 0) {
                // we can add that particualr course

                q.push(i);
            }
        }

        // then we can start the bfs

        int taken = 0;

        while (!q.empty()) {
            //

            // we want to pop from the queue
            int node = q.front();
            q.pop();
            taken++;

            // explore the neighbors of node, decrease their indegree.
            // if 0, add to queue

            for (auto& nei : adj[node]) {
                indegree[nei]--;
                if (indegree[nei] == 0) {
                    // then we can push this one onto the queue
                    q.push(nei);
                }
            }
        }
        return (taken == numCourses);

        // TC: O(V + E) where V is the number of classes and E is the number of connections
        // SC: O(V+E) b/c we store V nodes + E edges in the adj graph (dominatated)
    }
};
