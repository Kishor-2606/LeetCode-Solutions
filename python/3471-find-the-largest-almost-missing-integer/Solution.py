class Solution(object):
    def largestInteger(self, nums, k):
        freq={}
        window_freq={}
        l=0
        r=k
        for i in nums[:k]:
            window_freq[i]=window_freq.get(i,0)+1
        
        for i in window_freq:
            freq[i]=freq.get(i,0)+1
        
        while(r<len(nums)):
            print(window_freq)
            window_freq[nums[l]]-=1
            window_freq[nums[r]]=window_freq.get(nums[r],0)+1
            if window_freq[nums[l]]==0:
                del window_freq[nums[l]]
            for i in window_freq:
                freq[i]=freq.get(i,0)+1
            l+=1
            r+=1 

        mx=-1
        for key,value in freq.items():
            if value==1 and mx<key:
                mx=key
        return mx

        

            
        