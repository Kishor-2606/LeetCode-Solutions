class Solution(object):
    def maxAlternatingSum(self, nums):
        alter=[i**2 for i in nums]
        alter=sorted(alter)
        ans=0
        end=len(nums)
        if (end)%2!=0:
            ans=ans+(alter[(end//2)])
        i=0
        end-=1
        while(i<len(nums)//2): 
            ans=ans+(alter[end])
            ans=ans-(alter[i])
            end-=1
            i=i+1
        return ans