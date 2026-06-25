class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can store the frequency of these elements in a hashmap


        # then we can iterate through the objects of the frequency in reverse sorted order.
        # using the frequency, we can index it

        # this is an O(n log n) for the sorting on the frequencies in the map

        # however, we can do a little better

        # we can use a heap to manage the frequencies
        # we can push the frequencies of the elements onto the min
            # then we can maintain the heap of size k
            # pop off any elements that would make it > k, so then we are always popping the lowest frequency ones


        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        # now we have the freq in freq map
        # we want to build a min_heap and push all of the frequencies on
        # python's default heap is a minheap

        heap = []

        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))

            while len(heap) > k:
                heapq.heappop(heap)

        # finally , we want to build our solution
        res = []

        while len(heap) > 0:
            res.append(heapq.heappop(heap)[1]) # O(log k)

        return res
        

