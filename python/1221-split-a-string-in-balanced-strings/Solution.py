class Solution(object):
    def balancedStringSplit(self, s):
        cnt=0
        zeros=0
        i=0
        while(i<len(s)):
            if s[i]==s[0]:cnt+=1
            else:cnt-=1
            if cnt==0: zeros+=1
            i+=1
        return zeros
        
            