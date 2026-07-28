class Solution(object):
    def reversePrefix(self, s, k):
        return s[k-1::-1]+s[k:]
        