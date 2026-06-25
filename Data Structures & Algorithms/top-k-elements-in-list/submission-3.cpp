class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // put all of the numbers into a map
        // in C++, no defaultdict is required
        // we just need to define the key and value types

        unordered_map<int, int> count;
        for (int num: nums) {
            count[num]++;
        }

        // declare min heap - so we can easily evict the lowest freq pair
        priority_queue<pair<int, int>, vector<pair<int, int>> , greater<pair<int, int>>> heap;

        for (auto& entry : count) {
            // load the values into the heap
            heap.push({entry.second, entry.first});
            // if capacity overflows, we can evict the top using heap.pop()
            // it knows it's a heap so pop is enough
            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<int> res;

        for (int i = 0; i < k; i++) {
            // damn we can actually call the top and second like that
            res.push_back(heap.top().second);
            heap.pop();
        }

        return res;



    }
};
