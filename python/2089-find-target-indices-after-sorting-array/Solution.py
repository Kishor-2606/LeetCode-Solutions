class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        index=[]
        for i in range(len(nums)):
            if nums[i]==target:
                index.append(i)
        return index
        