class Solution(object):
    def minWindow(self, s, t):
        if s==t:
            return s
        freq={}
        l=0
        r=0
        subs=""
        mn_len=1000000000000
        memory=1000000000000
        need={}
        cnt=0
        for c in t:
            need[c]=need.get(c,0)+1
        req=len(need)
        while r<len(s):
            if s[r] in need and memory!=r:
                memory=r
                freq[s[r]]=freq.get(s[r],0)+1
                if freq[s[r]]==need[s[r]]:
                    cnt+=1   

            if cnt==req:
                if mn_len>r+1-l:
                    mn_len=r+1-l
                    subs=s[l:r+1]
                if s[l] in freq:
                    freq[s[l]]-=1
                    if freq[s[l]]<need[s[l]]:
                        cnt-=1
                    if freq[s[l]]==0:
                        del freq[s[l]]
                l=l+1
            else:
                r+=1
        return subs