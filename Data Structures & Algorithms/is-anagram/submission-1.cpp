class Solution {
public:
    bool isAnagram(string s, string t) {
        // compare the frequencies of the elements? 

        // we can use a single hashmap 
        // first word inc
        // second word dec

        // all values should be 0

        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> m;

        for (auto& c : s) {
             m[c]++;
        }

        for (auto& c2 : t) {
            m[c2]--;
        }


        // we can just iterate through the map directly

        for (auto& [k,v] : m) {
            if (v != 0) {
                return false;
            }
        }
        return true;


    }
};
