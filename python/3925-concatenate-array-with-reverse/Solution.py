class Solution(object):
    def concatWithReverse(self, nums):
        i=len(nums)-1
        while(i!=-1):
            nums.append(nums[i])
            i=i-1
        return nums
        
        