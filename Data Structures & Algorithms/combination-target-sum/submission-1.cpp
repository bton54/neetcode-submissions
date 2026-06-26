class Solution {
public:

    // we need to define a global variable
    vector<vector<int>> v;

    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        // we should keep adding the same value until exhasution (goes over)

        // do this recursively.

        vector<int> curr;

        dfs(0, curr, 0, nums, target);

        return v;
    }

private:

    // pass in a copy for index, reference everything else
    void dfs(int index, vector<int>& curr, int total, vector<int>& nums, int& target) {

        // check if we're end condition (outside of index or complete)

        if (index == nums.size() || total > target) {
            return;
        }
        if (total == target) {
            v.push_back(curr);
            return;
        }

        // now, for each value we want to add it and then go through the other values as well

        for (int i = index; i < nums.size(); ++i) {
            // add the current index and recurse
            curr.push_back(nums[i]);
            dfs(i, curr, total + nums[i], nums, target);

            // pop and then try another value, although i don't think we need to explicilty recurse here.
            curr.pop_back();

            // try the next value
        }

    }
};
