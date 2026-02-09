class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [nums[0] for nums in Counter(nums).most_common(k)]
    