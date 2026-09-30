class Solution(object):
    def majorityElement(self, nums):
        candy=0
        cnt=0
        for i in nums:
            if cnt==0:
                candy=i
            if candy==i:
                cnt+=1
            else:
                cnt-=1
        return candy
            