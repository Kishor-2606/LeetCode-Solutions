class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        divs=0
        for i in range(len(nums)):
            if nums[i]%3!=0:
                divs+=1
        return divs
        