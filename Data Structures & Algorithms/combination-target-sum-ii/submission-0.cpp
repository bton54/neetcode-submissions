class Solution {
public:


    vector<vector<int>> v; // stores sol

    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        // this way we want to use a dfs function to solve this one
        // store a public class result vector of solutions

        // use a dfs backtracking function
            // define base cases:
                // over target
                // out of numbers
            // for this one - we need to skip duplicates

        // we need to sort + add logic to skip duplicates
        sort(candidates.begin(), candidates.end());

        vector<int> curr_list;
        dfs(0, 0, curr_list, candidates, target);
        return v;
    }


    // make the index a copy and curr pass as value to copy
    // we can just reference candidates and the target value
    void dfs(int index , int curr_sum, vector<int> curr_list, vector<int>& candidates, int& target) {
        // base cases



        if (curr_sum > target) {
            return;
        }

        // valid solution
        if (curr_sum == target) {
            // we can copy this into the list and then return it? 
            v.push_back(curr_list);
            return;
        }

        if (index == candidates.size()) {
            return;
        }

        // now we want to dfs explore this

        // at each step, we either take or don't. we cannot re-use the same element

        curr_list.push_back(candidates[index]); 
        curr_sum += candidates[index];

        // recurse

        dfs(index + 1, curr_sum, curr_list, candidates, target); 

        // pop and advance to next

        curr_list.pop_back();
        curr_sum -= candidates[index];


        // we need to skip duplicates
        while (index < candidates.size() - 1 && candidates[index] == candidates[index+1]) {
            index++;
        }

        dfs(index + 1, curr_sum, curr_list, candidates, target);
    }


};
