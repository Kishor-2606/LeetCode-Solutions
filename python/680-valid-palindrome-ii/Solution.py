class Solution(object):
    def is_palindrome(self,s,st,en):
        while(st<en):
            if s[st]!=s[en]:
                return False
            st=st+1
            en=en-1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s=="":
            return False
        elif len(s)==1:
            return True
        elif len(s)==2:
            return True
        elif len(s)==3:
            return s[0]==s[2]
        else:
            i=0
            j=len(s)-1
            while(i<j):
                if s[i]==s[j]:
                    pass
                else:
                    if(self.is_palindrome(s,i+1,j) or self.is_palindrome(s,i,j-1)):
                        return True
                    else:
                        return False
                i=i+1
                j=j-1
            return True
                    
