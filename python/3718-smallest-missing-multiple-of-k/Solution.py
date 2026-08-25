class Solution(object):
    def missingMultiple(self, nums, k):
        n=k
        while(True):
            if n in nums:
                n=n+k
            else:
                return n