class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        my_dict={}
        ans=[]
        for num in nums:
            my_dict[num]=my_dict.get(num,0) +1
        for k,v in my_dict.items():
            if v==1:
                ans.append(k)
        return ans 