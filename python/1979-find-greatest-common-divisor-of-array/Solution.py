class Solution(object):

    def gcds(self,a,b):
        while b:
            a,b=b,a%b
        return a

    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return self.gcds(nums[0],nums[-1])
        
        