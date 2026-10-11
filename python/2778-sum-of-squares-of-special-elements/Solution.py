class Solution(object):
    def sumOfSquares(self, nums):
        sm=0
        n=len(nums)
        for i in range(len(nums)):
            if n%(i+1)==0:
                sm+=nums[i]**2
        return sm