class Solution(object):
    def minOperations(self, nums, k):
        sm=sum(nums)
        if sm<k:
            return sm
        elif sm%k==0:
            return 0
        else:
            return sm%k
        