class Solution(object):
    def reverseDegree(self, s):
        sm=0
        k=1
        for i in s:
            sm+=(k*(27-(ord(i)-96)))
            k=k+1
        return sm