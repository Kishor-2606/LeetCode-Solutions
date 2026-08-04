class Solution(object):
    def findLHS(self, nums):
        freq={}
        for i in nums:freq[i]=freq.get(i,0)+1
        mx=0
        for key in freq:
            if freq.get(key+1,0):
                mx=max(mx,freq[key]+freq[key+1])
        return mx
            
        