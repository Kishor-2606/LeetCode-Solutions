class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        ones=s.count('1')
        l=0
        r=n-1
        while l<n and s[l]=='1':
            l+=1
        while r>=0 and s[r]=='1':
            r-=1
        if l>r:
            return ones
        runs=[]
        length=1
        for i in range(l+1,r+1):

            if s[i]==s[i-1]:length+=1
            else:
                runs.append((length,s[i-1]));length=1
        runs.append((length,s[r]))
        max_gain=0
        for i in range(0,len(runs)-2,2):
            gain=runs[i][0]+runs[i+2][0]
            if gain>max_gain:max_gain=gain
        return ones+max_gain