class Solution(object):
    def minMoves(self, nums):
        mx=max(nums)
        final=0
        for i in nums:
            final+=abs(i-mx)
        return final

        