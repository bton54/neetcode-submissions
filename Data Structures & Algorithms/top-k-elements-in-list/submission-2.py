class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a heap - the k sized invariant
            # in short, given a set of frequencies, we can maintain the top k highest frequencies
            # when we exceed capacity, shave off the lowest frequencie sin the heap
                # the min heap nature can help us here - it keeps the lowest freq at the top + sorted

        # operations in heap are log k


        # in this case - we can iterate through nums, get the freqs of each element
        # then we can pass them into the heap
            # if we exceed length of k in the heap, pop the top (lowest freq)
            # adding elements to the heap via heappush always sorts (highest frequencies are pushed deeper)


        # TC: O(n log k) for the heap opertions + O(n) for getting the freqs
        # TC: O(n + k) for the map storing n frequencies and k for the heap storing k # of values


        # get the frequencies
        freq_map = defaultdict(int)

        for num in nums:
            freq_map[num] += 1

        # so this stores the number -> frequency

        heap = []

        for num, freq in freq_map.items():
            # this is heap syntax
            # also push it by freq as the leading key in the heap
            # no negation - the top element is always the lowest frequency value
            heapq.heappush(heap, (freq, num))


            if len(heap) > k:
                heapq.heappop(heap)

        # now we need to return the values in the heap

        res = []

        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res

        