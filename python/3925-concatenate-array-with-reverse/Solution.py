class Solution(object):
    def concatWithReverse(self, nums):
        copy=nums[:]
        copy.reverse()
        return nums+copy
        
        