class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        cnt=0
        for i in range(len(s)):
            if s[-(i+1)]!=" ":
                cnt+=1
            else:
                return cnt
        return cnt

        