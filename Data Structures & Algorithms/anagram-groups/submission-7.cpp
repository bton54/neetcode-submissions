class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // we want to store htem in an ungrouped map using the sorted anagram as a key

        // but sorting them each would be expensive, where m * n log n for the sorting 

        // thats okay tho lol

        unordered_map<string, vector<string>> mp;


        for (auto& str : strs) {
            string unsorted = str;
            sort(str.begin(), str.end());

            mp[str].push_back(unsorted);
        }

        // now we just need to dump the values

        vector<vector<string>> res;

        // iterate through the values:


        // does auto infer the vector map type? 
        for (auto& [k, v] : mp) {
            res.push_back(v);

        }

        return res;
    }
};
