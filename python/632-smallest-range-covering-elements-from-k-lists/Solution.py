from collections import defaultdict

class Solution:
    def smallestRange(self, nums):
        arr=[]

        for list_idx,lst in enumerate(nums):
            for num in lst:
                arr.append((num,list_idx))

        arr.sort()
        left=0
        covered=0
        freq=defaultdict(int)
        answer=[]

        for right in range(len(arr)):
            value,idx=arr[right]

            if freq[idx]==0:
                covered+=1
            freq[idx]+=1

            while covered==len(nums):
                start_value=arr[left][0]
                end_value=value

                if not answer or end_value-start_value<answer[1]-answer[0]:
                    answer=[start_value,end_value]

                freq[arr[left][1]]-=1
                if freq[arr[left][1]]==0:
                    covered-=1
                left+=1
        return answer