class Solution(object):
    def isPowerOfThree(self, n):
        if n==1 or n==3:
            return True
        if n<3 or n%3!=0:
            return False

        four=3
        while True:
            if n==four:
                return True
            elif four>n:
                return False
            four*=3
        