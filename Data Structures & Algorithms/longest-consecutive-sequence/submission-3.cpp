class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // possible solution
            // load values into set
            // check if the value +1 exists? and just keep going until it doesntt 
            // record the max length

        // time complexity - you add every element to the set once O(n)
        // then you run this check every element. 

        // optimal way - you only start counting if you find a start of a sequence
            // detect if n-1 exists in the set 
        
            // otherwise skip

        unordered_set<int> s;
        for (auto& num : nums) {
            s.insert(num);
        }
        
        int res = 0;

        for (int i = 0; i < nums.size(); ++i) {
            // we check if it's the start of the sequence
            if (s.count(nums[i] - 1) == 0) {
                // it is the start the sequence, keep going right? 

                int curr = nums[i];
                int temp = 1;

                while (s.count(curr + 1) > 0) {
                    temp++;
                    curr++;
                }

                res = max(res, temp);
            }
        }

        return res;
    }
};
