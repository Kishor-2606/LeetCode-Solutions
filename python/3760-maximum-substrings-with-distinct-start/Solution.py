class Solution(object):
    def maxDistinct(self, s):
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        return len(freq)
        