class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // We can use a set to determine if we added it
        unordered_set<int> seen;

        // iterate through the elements - if we've seen one before return true; otherwise return false;

        // use the auto iterator
        for (auto& x : nums){
        	if (seen.count(x) > 0) {
        		return true;
        	}
        	seen.insert(x);
        }
        return false;
    }
};