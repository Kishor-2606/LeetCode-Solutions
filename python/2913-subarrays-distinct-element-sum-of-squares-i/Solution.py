class Solution(object):
    def sumCounts(self, nums):
        i=0
        j=0
        ln=len(nums)
        st=set()
        cnt=0
        sm=0
        while(i<ln):
            if nums[j] not in st:
                st.add(nums[j])
                cnt+=1
            sm+=cnt**2
            j=j+1
            if j==ln:
                i=i+1
                j=i
                cnt=0
                st.clear()
        return sm

