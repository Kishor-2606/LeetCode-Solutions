class Solution(object):
    def findRepeatedDnaSequences(self, s):
        seen=set()
        ans=set()
        ln=len(s)
        l=0
        r=10
        while(r<=ln):
            st=s[l:r]
            if st in seen:
                ans.add(st)
            else:
                seen.add(st)
            l+=1
            r+=1
        return list(ans)    