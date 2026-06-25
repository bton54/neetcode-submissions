class Solution {
public:
    int findMin(vector<int> &nums) {
        // we want to use search in split half
        // binary search is required b/c of log n time requirement

        // we want to take the midpoint and then compare it to the end of the array
        // if it's greater than the end, that means the rotation cutoff is inbetween, search this side
        // otherwise, search the other half

        int l = 0;
        int r = nums.size() - 1;

        // we want to converge on a value, rather than are searching for something exact
            // for this, we would've used <= and r = mid + 1 
        // we want to converge on the minimum in this case, exclude mid
            // for this, l < r and r = mid

        while (l < r) {
            int m = (l + r) / 2;

            if (nums[m] > nums[r]) {
                // we should search the right side
                l = m + 1;
            }
            else {
                r = m;
            }
        }
        // this should converge on the right pointer
        return nums[l];
    }
};
