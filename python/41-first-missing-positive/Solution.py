class Solution(object):
    def firstMissingPositive(self, nums):
        nums=set(nums)
        i=1
        while True:
            if (i not in nums) or (i+1 not in nums):
                if i not in nums:return i
                return i+1
            i+=2