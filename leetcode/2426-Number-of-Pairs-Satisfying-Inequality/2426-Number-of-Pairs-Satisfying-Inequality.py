class Solution(object):
    def numberOfPairs(self, nums1, nums2, diff):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type diff: int
        :rtype: int
        """
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        
        count = 0
        seen = SortedList()
        
        for val in a:
            count += seen.bisect_right(val + diff)
            seen.add(val)
            
        return count