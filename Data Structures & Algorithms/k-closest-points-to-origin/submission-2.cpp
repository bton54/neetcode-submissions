class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // we can load all of the points based on distance into a min heap
        // then, we can pop off the top / lowest ones

        // max heap
        priority_queue<pair<int, vector<int>>> heap;
        // {distance, point}

        // iterate through the points 
        for (const auto& point : points) {
            int x = point[0];
            int y = point[1];

            int dist = x * x + y * y;
            heap.push({dist, point});

            if (heap.size() > k) {
                heap.pop();
            }
        }


        vector<vector<int>> res;

        while (!heap.empty()) {
            auto top = heap.top();
            heap.pop();
            res.push_back(top.second);
        }

        return res;
    }
};
