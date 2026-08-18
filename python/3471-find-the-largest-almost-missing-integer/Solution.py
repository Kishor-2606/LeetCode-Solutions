class Solution(object):
    def largestInteger(self, nums, k):
        seen=set()
        freq={}
        i=0
        j=0
        cnt=0
        while(j<len(nums)):
            if cnt==k:
                i=i+1
                j=i-1
                cnt=-1
                seen.clear()
            elif nums[j] not in seen:
                freq[nums[j]]=freq.get(nums[j],0)+1
                seen.add(nums[j])
            j=j+1
            cnt+=1
        mx=-1
        mn=10000
        for key,value in freq.items():
            if value==1 and mx<key:
                mx=key
                mn=value
        return mx

        

            
        