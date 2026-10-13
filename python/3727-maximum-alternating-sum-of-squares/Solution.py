class Solution(object):
    def maxAlternatingSum(self, nums):
        alter=[i**2 for i in nums]
        alter=sorted(alter)
        start=0
        end=len(nums)-1
        ans=0
        i=0
        while(i<len(nums)//2): 
            ans=ans+(alter[end])
            ans=ans-(alter[start])
            end-=1
            start+=1
            i=i+1
        if len(nums)%2!=0:
            return ans+(alter[(len(nums)//2)])
        return ans