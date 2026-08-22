class Solution(object):
    def countKConstraintSubstrings(self, s, k):
        freq={}
        l,r=0,0
        cnt=0
        memory=100
        while(l<len(s) and r<len(s)):
            if r<len(s) and r!=memory:
                memory=r
                freq[s[r]]=freq.get(s[r],0)+1
            if (freq.get('1',0)<=k or freq.get('0',0)<=k) and r<len(s)-1:
                r=r+1
            elif (freq.get('1',0)>k and freq.get('0',0)>k):
                cnt+=freq.get('0',0)+freq.get('1',0)-1
                freq[s[l]]-=1
                l=l+1
            else:
                if (r==len(s)-1):
                    cnt+=freq.get('0',0)+freq.get('1',0)
                    freq[s[l]]-=1
                    l=l+1
        return cnt
            


        