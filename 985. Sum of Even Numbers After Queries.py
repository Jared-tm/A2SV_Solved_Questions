class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        even_sum=  0
        for num in nums:
            if num%2 == 0:
                even_sum += num
        ans=[]
        for a,i in queries:
            if nums[i]%2 == 0:
                even_sum -= nums[i]
            nums[i] += a
            if nums[i] %2 ==0:
                even_sum += nums[i]                  
            ans.append(even_sum)

        return ans
        