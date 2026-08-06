class Solution(object):
    def smallestNumber(self, n, t):
        if '0' in str(n):
            return n
        while True:
            product=1
            for i in str(n):
                product*=int(i)
            if product%t==0:
                return n
            n=n+1



        