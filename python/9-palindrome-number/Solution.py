class Solution(object):
    def isPalindrome(self, x):
        st=str(x)
        return st==st[::-1]