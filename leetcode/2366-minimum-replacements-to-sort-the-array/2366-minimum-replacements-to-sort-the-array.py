class Solution(object):
    def minimumReplacement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations = 0
        lim = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] > lim:
                k = (nums[i]+lim-1) // lim
                operations += k-1
                lim = nums[i]//k
            else:
                lim = nums[i]
        return operations
            


        