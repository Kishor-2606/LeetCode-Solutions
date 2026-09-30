class Solution(object):
    def majorityElement(self, nums):
        freq={}
        mx=0
        k=0
        for i in nums:
            freq[i]=freq.get(i,0)+1
            if freq[i]>mx:
                k=i
                mx=freq[i]
        return k