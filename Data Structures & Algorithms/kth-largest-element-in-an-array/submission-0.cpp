class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // we want to load the elements into a min heap
        // then, we can just evict up to the kth value.

        // alternatively, we can maintain a heap of size k and simply evict elements that go over the size

        // we simply want to store numbers, and b/c we want to use a min hea pwe have to specifiy
        // C++ PQ is default max heap
        priority_queue<int , vector<int> , greater<int>> pq; 

        // now we want to load up the values
        

        for (auto& num : nums) {
            // iterate through the numbers

            pq.push(num); 

            if (pq.size() > k) {
                // top_val = pq.top(); not needed to record this lmfao
                pq.pop();
            }


        }

        return pq.top();
    }
};
