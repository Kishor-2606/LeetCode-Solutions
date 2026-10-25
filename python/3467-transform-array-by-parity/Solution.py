class Solution(object):
    def transformArray(self, nums):
        odd=0
        eve=0
        for i in nums:
            if i%2==0:
                eve+=1
            else:
                odd+=1
        return ([0]*eve)+([1]*odd)
        