class Solution(object):
    def isPerfectSquare(self, num):
        start=1
        end=num//2
        while start<=end:
            middle=(start+end)//2
            power=middle*middle
            if power>num:
                end=middle-1
            elif power<num:
                start=middle+1
            else:
                return True
        return num==1

        