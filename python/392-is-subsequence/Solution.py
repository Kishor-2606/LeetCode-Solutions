class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        cnt=0
        if s=="":
            return True
        while(i<len(s) and j<len(t)):
            if s[i]!=t[j]:
                j=j+1
            else:
                cnt+=1
                i=i+1
                j=j+1
            if cnt==len(s):
                return True
        print(i,j)
        print(cnt)
        return False
        