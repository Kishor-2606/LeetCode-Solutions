class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        left=0
        right=0
        freq={}
        hs=set()
        while(True):
            if freq.get('1',0)==k:
                hs.add(s[left:right])
                freq[s[left]]=freq[s[left]]-1
                left=left+1
            else:
                freq[s[right]]=freq.get(s[right],0)+1
                right=right+1
            if right==len(s) and freq.get('1',0)<k:
                break
        if len(hs)==0:
            return ""
        st="Z"
        sml_len=1000000
        for i in hs:
            if len(i)<sml_len:
                sml_len=len(i)
        for i in hs:
            if len(i)==sml_len:
                st=min(st,i)
        return st

        
        