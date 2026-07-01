class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // sort by end time
        // iterate through the intervals
        // add the first interval to the new list
        // and then compare it

        // TC: O(n log n ) 
        // SC: O(n) solution array

        sort(intervals.begin(), intervals.end()); 
        // sort(intervals.begin(), intervals.end(), [](auto&a , auto&a 
        // ) { a[0] < b[0]}); 

        vector<vector<int>> res;
        // we want to add the first interval
        res.push_back(intervals[0]); 


        // and then we want to iterate through the remaining and compare to res

        for (int i = 1; i < intervals.size(); ++i) {
            // we want to compare this to the last interval
            vector<int> last_interval = res[res.size() - 1]; 

            vector<int> curr_interval = intervals[i];

            // check if end time of last over laps with start of curr

            if (last_interval[1] >= curr_interval[0]) {
                // we can merge them

                res[res.size() - 1] = { min(last_interval[0], curr_interval[0]), max(last_interval[1], curr_interval[1]) };
            }

            // there's no overlap

            else {
                // can just append
                res.push_back(curr_interval);
            }
        }

        return res;
    }
};
