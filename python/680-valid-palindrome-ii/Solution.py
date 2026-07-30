class Solution(object):
    def is_palindrome(self,s,st,en):
        while(st<en):
            if s[st]!=s[en]:
                return False
            st=st+1
            en=en-1
        return True
    def validPalindrome(self, s):
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return (self.is_palindrome(s,i+1,j) or self.is_palindrome(s,i,j-1))
            i=i+1
            j=j-1
        return True