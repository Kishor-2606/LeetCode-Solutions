class Solution(object):
    def twoSum(self, nums, target):
        dick={}
        i=0
        while i<len(nums):
            val=target-nums[i]
            if val in dick:
                return [dick[val],i]
            dick[nums[i]]=i
            i+=1
        