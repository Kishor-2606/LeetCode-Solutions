class Solution(object):
    def canBeEqual(self, target, arr): 
        freq={}
        for i,j in zip(target,arr):
            freq[i]=freq.get(i,0)+1
            freq[j]=freq.get(j,0)-1

        return all(v==0 for v in freq.values())