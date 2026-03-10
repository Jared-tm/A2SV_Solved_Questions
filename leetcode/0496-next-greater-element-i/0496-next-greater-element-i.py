class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = defaultdict(lambda:-1)

        for num in nums2:
            while stack and  num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        return [ next_greater[num] for num in nums1]



        