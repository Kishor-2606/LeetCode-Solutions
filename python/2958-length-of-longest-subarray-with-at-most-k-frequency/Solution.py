class Solution(object):
    def maxSubarrayLength(self, nums, k):
        n = len(nums)
        r = 1
        for left in range(n):
            freq = {}
            for right in range(left, n):
                c = nums[right]
                freq[c] = freq.get(c, 0) + 1
                if freq[c] > k:
                    break
                r = max(r, right - left + 1)
        return r
        
        