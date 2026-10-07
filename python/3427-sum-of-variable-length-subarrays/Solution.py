class Solution:
    def subarraySum(self, nums):
        n=len(nums)
        total_sum=0
        for i in range(n):
            start=max(0,i-nums[i])
            for j in range(start,i+1):
                total_sum+=nums[j]
        return total_sum