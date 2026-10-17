class Solution(object):
    def firstMissingPositive(self, nums):
        nums=set(nums)
        for i in range(1,100002):
            if i not in nums:
                return i