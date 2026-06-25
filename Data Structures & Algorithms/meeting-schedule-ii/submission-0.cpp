/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {

    	// sort in c++ the intervals by start time
    	sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
    		// custom syntax to sort by start times
    		return a.start < b.start; 
    	});

    	// define a min heap
    	priority_queue< int, vector<int> , greater<int>> minHeap;

    	// iterate through the intervals
    	for (const auto& interval : intervals) { 
    		// if we have values in the min heap and the current meeting (on heap) ends before the next
    		if (!minHeap.empty() && minHeap.top() <= interval.start) {
    			minHeap.pop();
    		}
    		// push end time onto the heap regardless - this is how we determine # of required rooms
    		minHeap.push(interval.end);
    	}
    	return minHeap.size(); 

    }
};
