class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        // bro wants to eat as slow as possible.
        // the slowest he can eat is the rate of the largest pile
        // the fastest he can eat is what we're trying to calculate.

        // we should start at the slowest and binary search a feasibility function (binary search on answer) 

        int slowest_speed = *max_element(piles.begin(), piles.end());

        // 

        int l = 1;
        int r = slowest_speed;

        while (l < r) {
            // we want them to converage ultimately, not some mystery value

            int m = (l+r) / 2; // this does int division per the type

            if(isPossible(piles, h, m)) {
                // if that speed IS possible, then we can adjust the speed of r (to see if we can eat slower)
                r = m;
            }
            else {
                // otherwise, we can move up the r pointer
                l = m+1;
            }
        }
        return l; // this should converge to l.


    }

    bool isPossible(vector<int>& piles, int h, int k) { 
        // we need to go through the banana piles basically and see how many times it takes for them to eat
        // we need to go through the piles and increment

        // this sum can > 2b, use long long 
        long long time_required = 0;

        for (auto& pile : piles) {
            time_required += (pile + k - 1) / k;

            // ex. (10 + 3 - 1) / 3 would yield 4; it would indeed take 4 hours to eat 10 bananas.
            // adding k - 1 triggers another cycle in the case of remainders.
        }

        return (time_required <= h);

        // if (time_required > h) {
        //     return false;
        // }
        // return true;

    }
};
