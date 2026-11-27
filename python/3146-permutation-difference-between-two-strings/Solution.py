class Solution(object):
    def findPermutationDifference(self, s, t):
        sm=0
        freq={}
        for i in range(len(s)):
            freq.setdefault(s[i],[]).append(i)
            freq.setdefault(t[i],[]).append(i)
        
        for key,value in freq.items():
            sm+=abs(value[0]-value[1])

        return sm