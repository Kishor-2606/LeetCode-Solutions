class Solution(object):
    def maxProduct(self, nums):
        pref=0
        suff=0
        maxi=-10000
        for i in range(len(nums)):
            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref*=nums[i]
            suff*=nums[len(nums)-1-i]
            maxi=max(max(pref,suff),maxi)
        return maxi