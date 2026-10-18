class Solution(object):
    def findLengthOfLCIS(self, nums):
        ln=0
        mx=1
        i=0
        while(i<len(nums)-1):
            if nums[i]<nums[i+1]:
                ln+=1
            else:
                ln=0
            i=i+1
            mx=max(mx,ln+1)
        return mx
