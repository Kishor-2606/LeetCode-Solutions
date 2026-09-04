class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        lows=[0]*n
        lows[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            lows[i]=min(nums[i],lows[i+1])
        high=nums[0]
        for i in range(n):
            high=max(high,nums[i])
            if high-lows[i]<=k:
                return i
        return -1