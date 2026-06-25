import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # We constantly need to get the two heaviest stones inside of the list
        # If we want to prioritize by weight, we can use some data structure that has priority
        # A heap (max heap) is perfect
        # we can load all of the stones onto the heap.
        # this will cost O(n log k) time, where k is the number of elements in the heap at a time

        # we need to add the weights on the stones in reverse order since python default heap is a min heap

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1 = -(heapq.heappop(heap))
            stone2 = -(heapq.heappop(heap))

            # if weights are even
            if stone1 == stone2:
                continue
                # they both break, we continue

            # other cases
            if stone1 > stone2:
                stone1 -= stone2
                heapq.heappush(heap, -stone1)

            else:
                stone2 -= stone1
                heapq.heappush(heap, -stone2)

        return -heap[-1] if len(heap) == 1 else 0
            

