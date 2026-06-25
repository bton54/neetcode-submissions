class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // we need to sort the list
        // then we just like increment inwards

        int l = 0;
        int r = numbers.size() - 1;

        //

        while (l < r) {
            //

            int s = numbers[l] + numbers[r];
            if (s == target) {
                return {l+1, r+1}; // think we have to return it like this? to simulate vector
            }
            if (s > target) {
                // we overshoot, shift the right
                r--;
            }
            else {
                l++;
            }
        }
    }
};
