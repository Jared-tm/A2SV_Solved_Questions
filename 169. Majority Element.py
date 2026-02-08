class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        m = len(nums)/2
        for k,v in freq.items():
            if v > m:
                return k 