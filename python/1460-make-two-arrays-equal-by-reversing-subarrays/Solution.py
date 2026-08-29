class Solution(object):
    def canBeEqual(self, target, arr):
        freq={}
        for i,j in zip(target,arr):
            freq[i]=freq.get(i,0)+1
            freq[j]=freq.get(j,0)-1
            
        for value in freq.values():
            if value!=0:
                return False
        return True

        # arr=sorted(arr)
        # target=sorted(target)
        # return arr==target
        