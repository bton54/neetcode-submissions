class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // we want to sort the intervals by start time
        sort(intervals.begin(), intervals.end());

        // then we want to iterate through the intervals.
        // for each interval, if the previous one overlaps, we can merge it ... get a fresh list with the first interval
        vector<vector<int>> v;

        v.push_back(intervals[0]);

        // now iterate through the remaining and compare

        for (int i = 1; i < intervals.size(); ++i) {
            // now we can go

            vector<int> interval = intervals[i];

            // now we can pull the start, end from this one using [0] [1]

            // you can't just do Python v[-1] XD
            vector<int> prev_interval = v[v.size() - 1]; 

            // if the prev end time overlaps with the curr start time
            if (prev_interval[1] >= interval[0]) {
                vector<int> new_interval = { min(prev_interval[0], interval[0]) , max(prev_interval[1], interval[1])};

                v.pop_back();
                v.push_back(new_interval);



            }

            else {
                // if there's no overlap, just append
                v.push_back(interval);
            }


        }

        return v;
    }
};
