class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;

        while (l <= r) {
            // we want to keep the mid point as a valid

            int m = (l+r) / 2;

            if (nums[m] == target) {
                // we want to return the index
                return m;
            }

            if (nums[l] <= nums[m]) {
                // this is the sorted side
                // check if the target is in the sorted range (aka if it's < the mid)
                if (target > nums[m] || target < nums[l]) {
                    // if so we can search the left half.
                    // move the right pointer
                    l = m + 1; // we move it past m
                    // we do r = m to retain m in search space if not looking for specific value
                }
                else {
                    //move the left pointer
                    r = m - 1;
                }

            }
            else {
                // the right half if sorted

                // check if the target > mid
                if (target < nums[m] || target > nums[r]) {
                    // then we can search the left half
                    r = m - 1;
                }
                else {
                    l = m + 1;
                }
            }
        }

        return -1; // edgecase
    }
};
