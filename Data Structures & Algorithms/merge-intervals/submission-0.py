class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we want to sort the intervals by their start time
        # then we can go through the list of intervals
            # compare the current one's start to the previous interval's end
                # if they overlap, combine them
            # we should also start at the 2nd interval (index 1)
        # TC: O(n log n) dominated by the sorting

        # sort by the start time - i'm not sure why...
        # intervals.sort(lambda x: x[0])
        intervals.sort()

        res = []

        res.append(intervals[0])

        for i in range(1, len(intervals)):
            # if the end time of the previous one is > the start time of the current one - merge them
            if res[-1][1] >= intervals[i][0]:
                # merge them
                res[-1][0] = min(res[-1][0] , intervals[i][0])
                res[-1][1] = max(res[-1][1] , intervals[i][1])

            else:
                # simply append this interval to the existing list
                res.append(intervals[i])

        return res


