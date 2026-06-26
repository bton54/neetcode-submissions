class Solution {
public:

    vector<vector<int>> res; // global variable


    vector<vector<int>> subsets(vector<int>& nums) {
        // we need to return possible subsets 
        // we want to explore this recursively
        // at each step, we can take the item or not. 
        // we need to define a dfs function
        vector<int> curr;
        dfs(0, curr , nums);
        return res;
    }

private:
    // the signature requires int index; a reference would fail. you want to copy here
    // recursion requires an index per call, hence requiring copying
    void dfs(int index, vector<int>& curr, vector<int>& nums) {
        // if we're at the end of the list
        if (index == nums.size()) {
            // we need to return a copy of thie curr into the res

            res.push_back(curr);
            return;
        }

        // we recurse 2x, one with taking, one with not

        curr.push_back(nums[index]); /// can't shortcut in Python by just passing curr.push_back(nums[i])
        dfs(index+1, curr, nums);

        // then we should pop
        curr.pop_back();
        dfs(index+1, curr, nums);

    }
};
