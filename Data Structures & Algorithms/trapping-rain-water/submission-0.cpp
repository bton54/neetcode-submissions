class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> st; // store index

        // iterate through the height 

        int res = 0;

        for (int i = 0; i < height.size(); ++i) {
            // monotonic stack
            // if there is an uptick in height, find the left bound
            while (!st.empty() && height[i] > height[st.top()]) {
                int bottom = st.top();
                st.pop();

                if (st.empty()) {
                    break;
                }

                int left = st.top();
                int width = i - left - 1;
                int boundedHeight = min(height[left], height[i]) - height[bottom];

                res += width * boundedHeight;
            }
            st.push(i);

        }
        return res;
    }
};
