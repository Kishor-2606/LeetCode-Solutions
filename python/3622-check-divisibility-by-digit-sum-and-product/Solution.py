class Solution(object):
    def checkDivisibility(self, n):
        sm=0
        prd=1
        copy=n
        digit=0
        while copy>0:
            digit=copy%10
            copy=copy/10
            sm=sm+digit
            prd=prd*digit
        return n%(sm+prd)==0