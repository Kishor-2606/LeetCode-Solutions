class Solution(object):
    def findMaxLength(self, nums):
        hashmap={}
        sm=0
        mx_len=0
        hashmap[0]=-1
        for i in range(len(nums)):
            if nums[i]==0:
                sm+=-1
            else:
                sm+=nums[i]
            if sm in hashmap:
                mx_len=max(mx_len,i-hashmap[sm])
            else:
                hashmap[sm]=i
        return mx_len

