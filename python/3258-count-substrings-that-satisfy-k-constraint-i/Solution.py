class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        freq={}
        l,r=0,0
        cnt=0
        while(l<len(s)):
            if l!=r:
                cnt+=1
            if r<len(s):
                freq[s[r]]=freq.get(s[r],0)+1
            if (freq.get('1',0)<=k or freq.get('0',0)<=k) and r<len(s):
                r=r+1
            elif (freq.get('1',0)>k and freq.get('0',0)>k) or (r==len(s)):
                freq.clear()
                l=l+1
                r=l    
        return cnt
            


        