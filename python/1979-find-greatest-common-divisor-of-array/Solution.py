
class Solution(object):

    def gcds(self,a,b):
        gcd=0
        for i in range(1,a+1):
            if a%i==0 or b%i==0:
                gcd=i
        return gcd

    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return self.gcds(nums[0],nums[-1])
        