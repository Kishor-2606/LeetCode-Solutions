class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in dic:
                return [dic[val],i]
            else:
                dic[nums[i]]=i