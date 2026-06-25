class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # well we can actually just maintain a heap of size k
        self.k = k
        self.heap = []

        for n in nums:
            heapq.heappush(self.heap, n)

        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:

        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]

        
