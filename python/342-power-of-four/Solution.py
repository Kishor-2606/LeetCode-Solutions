class Solution(object):
    def isPowerOfFour(self, n):
        if n==1:
            return True
        if n<4 or n%4!=0:
            return False

        four=4
        while True:
            if n==four:
                return True
            elif four>n:
                return False
            four*=4
        
             
        