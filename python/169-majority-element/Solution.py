class Solution(object):
    def majorityElement(self, nums):
        freq={}
        mx=0
        k=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key,value in freq.items():
            if value>mx:
                k=key
                mx=value
        return k