class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in nums:
            if nums.count(i)==2:
                nums.remove(i)
                ls.append(i)
        return ls