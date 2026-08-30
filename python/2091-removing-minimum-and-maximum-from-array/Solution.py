class Solution(object):
    def minimumDeletions(self, nums):
        index1=0
        index2=0
        mn=100000
        mx=-100000
        if len(nums)<3:
            return len(nums)
        for i in range(len(nums)):
            if nums[i]<mn:
                mn=nums[i]
                index1=i
            if nums[i]>mx:
                mx=nums[i]
                index2=i       
        copy=index1
        index1=min(index1,index2)
        index2=max(copy,index2)
        return min(index2+1,(index1+1)+(len(nums)-index2),len(nums)-index1)