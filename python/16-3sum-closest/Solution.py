class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        n=len(nums)
        diff=float('inf')
        res_sum=0
        for i in range(n-2):
            left=i+1
            right=n-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                d=abs(target-total)
                if d<diff:
                    diff=d
                    res_sum=total
                if total==target:
                    return total
                if total<target:
                    left+=1
                else:
                    right-=1
        return res_sum