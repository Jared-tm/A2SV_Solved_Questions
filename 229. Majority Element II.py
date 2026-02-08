class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        freq=Counter(nums)
        n=len(nums)/3
        ans=[]

        for k,v in freq.items():
            if v > n:
                ans.append(k)
        return ans
                
                