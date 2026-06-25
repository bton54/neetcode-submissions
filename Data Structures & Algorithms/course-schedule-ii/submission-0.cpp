class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // we need to run toplogical sort to see if we can run all of the courses

        vector<int> res;

        // we need a queue, adj_graph, and a indegree to run the top sort
        unordered_map<int, vector<int>> adj_graph;

        vector<int> indegree(numCourses); // init all courses with 0 indegree
        // we need to

        // build the adj_graph and update indegrees
        for (auto& prereq : prerequisites) {
            adj_graph[prereq[1]].push_back(prereq[0]);
            indegree[prereq[0]]++; // a has another class to depend on
        }

        // set up the queue
        queue<int> q;

        // only indegree elements with 0

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        // then we can run the topological sort

        while(!q.empty()) {
            // we can get the top node
            int node = q.front();
            q.pop();

            res.push_back(node);

            // we need to go through all the neighbors
            for (auto& nei : adj_graph[node]) {
                // we simply need to adjust the indegree, we don't care about manipualtion of the nodes
                
                indegree[nei]--;

                // if it hits 0 all prereqs are satisfied we can upload to q
                if (indegree[nei] == 0) {
                    q.push(nei);
                }
            }
        }
        if (res.size() == numCourses) {
            return res;
        }

        return {};
    }
};
