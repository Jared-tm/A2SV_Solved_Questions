from collections import Counter
class Solution:
    def minimumIndex(self, nums: list[int]) -> int:
        count = {}
        n = len(nums)
        for i in range(n):
           count[nums[i]]= count.get(nums[i], 0) + 1      
        
        for key,value in count.items():
            if 2*value > n:
                dom  = key
                break
            
        total_dom = count[dom]
        k = 0 
        for i in range(n - 1):
            if nums[i] == dom:
                 k += 1
            
            left_len = i + 1
            right_len = n - left_len
            
            if k * 2 > left_len and (total_dom - k) * 2 > right_len:
                 return i
        
        return -1
                 





if __name__ == "__main__":
    print(Solution().minimumIndex([1,2,2,2]))