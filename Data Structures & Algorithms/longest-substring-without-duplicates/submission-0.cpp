class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // sliding iwndow
        // slide the left window using a while function while the condition is met
        
        // use an unordered set to track the char
        unordered_set<char> st;

        int max_len = 0;


        int l = 0;

        // drive the right pointer using a for loop

        for (int r = 0; r < s.length(); r++) {
            // from where, we want to see if we can add the letter to the sub list

            // while the condition is invalid
            while (st.count(s[r]) > 0) {
                // we have to slide the left window
                st.erase(s[l]);
                l++;

            }

            // then we can just add to the set and update the counter

            st.insert(s[r]);
            // then we want to count the number of like values in the set at a time
            max_len = max(max_len, r-l+1);
        }

        return max_len;
    }
};
