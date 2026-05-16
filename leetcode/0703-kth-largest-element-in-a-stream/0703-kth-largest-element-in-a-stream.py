import heapq
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = nums
        
        
        heapq.heapify(self.min_heap)
        
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
    
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        
        return self.min_heap[0]