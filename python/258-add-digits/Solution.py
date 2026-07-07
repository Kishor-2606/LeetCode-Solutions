class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<10:
            return num
        digit_sum=0
        n=num
        while(n>9):
            digit_sum=0
            while(n!=0):
                digit_sum+=n%10
                n=n//10
            n=digit_sum

        return digit_sum
        

        