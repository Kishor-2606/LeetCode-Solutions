class Solution(object):
    def findMaxLength(self, nums):
        hashmap={}
        sm=0
        mx_len=0
        hashmap[0]=-1
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            sm+=nums[i]
            if sm in hashmap:
                mx_len=max(mx_len,i-hashmap[sm])
            else:
                hashmap[sm]=i
        if sm==0:
            return len(nums)
        return mx_len

