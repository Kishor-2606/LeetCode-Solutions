class Solution(object):
    def scoreOfString(self, s):
        score=0
        for i in range(1,len(s)):
            score+=abs(ord(s[i-1])-ord(s[i]))
        return score