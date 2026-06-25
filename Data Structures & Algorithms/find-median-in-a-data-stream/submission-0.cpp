#include <queue>
#include <vector>
class MedianFinder {
public:
    MedianFinder() {
        
    }

    // we need to use 2 heaps to solve this question
    // left max heap (stores lower values)
    // right min heap (stores higher max values)

    // allows us to take the top of each and get the value quickly
    priority_queue<int> l; // this is the max heap syntax by default
    // this gives min heap syntax if we use the greater - op of map
    priority_queue<int, vector<int>, greater<int>> r;

    // when we add nums, push it into the left heap

    // then we can check if the values are fked up (top of left > top right)
    // then we can rebalance based on size
    void addNum(int num) {
        l.push(num);

        // then we can check if the values are fked

        // if (r and l[0] > r[0]): swap them
        if (!r.empty()) {
            if (l.top() > r.top()) {
                // we can pop from the left and put into right

                // note we have to explicitly pull top and push
                int swap = l.top();
                l.pop();
                r.push(swap);
            }
        }

        // rotate for balance
        if (l.size() > r.size() + 1) {
            int swap = l.top(); 
            l.pop();
            r.push(swap);
        }
        else if (l.size() < r.size()) {
            // inverse case in case
            int swap = r.top();
            r.pop();
            l.push(swap);
        }
    }
    
    double findMedian() {
        if (l.size() > r.size()) {
            // we can just return this top one
            return l.top();
        }
        return ((l.top() + r.top()) / 2.0);
    }
};
