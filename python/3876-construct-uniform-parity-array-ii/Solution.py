class Solution(object):
    def uniformArray(self,nums1):
        min_val = min(nums1)
        if min_val % 2 != 0:
            return True
        return all(x % 2 == 0 for x in nums1)