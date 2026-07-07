class Solution(object):
    def sumAndMultiply(self, n):
        if n==0:
            return 0
        st=str(n).replace('0','')
        ad=0
        for i in st:
            ad+=int(i)
        return ad*(int(st))












            