class Solution {
public:

    vector<vector<int>> res;
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        
        if (nums.size() == 0) {
            return {};
        }

        // and then we can execute the recursive function
        vector<int> curr;
        sort(nums.begin(), nums.end());
        dfs(nums, curr, 0);
        return res;




    }

    // pass index as value
    // pass list as value

    // ref only for the nums
    void dfs(vector<int>&nums, vector<int> curr, int index) {
        // exit conditions

        // the way we'd handle this one would be to like simply sort and skip the repeats i believe. 

        // but the catch is that we must also use the existing value

        if (index == nums.size()) {
            res.push_back(curr); // we need to copy so since we pass by value this should be ok
            return;
        }

        curr.push_back(nums[index]);

        dfs(nums, curr, index + 1);

        // proceed without it

        curr.pop_back();

        // we just need to skip all duplicates
        int next_index = index + 1;

        while (next_index < nums.size() and nums[next_index] == nums[index]) {
            next_index++;
        }

        dfs(nums, curr, next_index); 
        

        
    }
};
