class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp; 

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            if (mp.count(complement) > 0) {
                return {mp[complement], i};
            }
            else {
                // add the index
                mp[nums[i]] = i;
            }
        }
    }
};
