class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // we can use topological sort using adj graph, indegree, queue

        // map the adj_graph
        unordered_map<int, vector<int>> adj_graph;

        // create indegree list with everything init to 0

        vector<int> indegree(numCourses, 0);

        // build the adj_graph and increment indegree

        for (auto& pre : prerequisites) {
            adj_graph[pre[0]].push_back(pre[1]);
            indegree[pre[1]]++;
        }

        // then build the queue
        queue<int> q;

        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }

        int res = 0;

        while (!q.empty()) {
            auto node = q.front();
            q.pop();

            res++;

            auto neighbors = adj_graph[node];

            for (auto& nei : neighbors) {
                indegree[nei]--;

                if (indegree[nei] == 0) {
                    q.push(nei);
                }
            }

        }

        return res == numCourses;
    }
};
