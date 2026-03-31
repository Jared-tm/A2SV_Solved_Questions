class Solution:
    def searchRange(self, nums , target):
        def findFirst(l, r):
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid
                    r = mid - 1 
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        def findLast(l, r):
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    ans = mid
                    l = mid + 1 
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
      
            
        first = findFirst(0, len(nums) - 1)
        last = findLast(0, len(nums) - 1)
        
        return [first, last]