class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans=[]
        self.solve(nums,target,4,[],ans)
        return ans

    def solve(self, nums, target, k, path, ans):
        if len(nums)<k:
            return

        if k==2:
            left=0
            right=len(nums)-1

            while left<right:
                total=nums[left]+nums[right]

                if total==target:
                    ans.append(path+[nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1

                elif total<target:
                    left+=1
                else:
                    right-=1
            return

        for i in range(len(nums)-k+1):
            if i>0 and nums[i]==nums[i-1]:
                continue

            if nums[i]*k>target:
                break
            if nums[-1]*k<target:
                break

            self.solve(nums[i+1:],target-nums[i],k-1,path+[nums[i]],ans)