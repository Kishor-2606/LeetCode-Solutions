class Solution(object):
    def findMissingElements(self, nums):
        st=[]
        m,n=min(nums),max(nums)
        nums=set(sorted(nums))
        for i in range(m+1,n):
            if i not in nums:
                st.append(i)
        return st