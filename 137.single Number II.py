class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict={}
        for num in nums:
            my_dict[num]=my_dict.get(num,0) +1
        for k,v in my_dict.items():
            if v==1:
                return k 
        