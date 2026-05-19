class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        heap = []
        
        for word, count in counts.items():
            heapq.heappush(heap, (-count, word))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result

        