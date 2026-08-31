class Solution(object):
    def runningSum(self, nums):
        prefix_sum=[]
        ps=0
        for i in nums:
            ps+=i
            prefix_sum.append(ps)
        return prefix_sum

        