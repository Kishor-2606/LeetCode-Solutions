class Solution(object):
    def minimumAverage(self, nums):
        min_avg = float('inf')
        nums.sort()
        j = len(nums) - 1

        for i in range(len(nums) // 2):
            avg = (nums[i] + nums[j]) / 2.0
            min_avg = min(avg, min_avg)
            j -= 1

        return min_avg
        