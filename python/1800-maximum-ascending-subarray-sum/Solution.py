class Solution(object):
    def maxAscendingSum(self, nums):
        sm=nums[0]
        mx_sm=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sm+=nums[i]
            else:
                sm=nums[i]
            mx_sm=max(mx_sm,sm)
        return mx_sm

        