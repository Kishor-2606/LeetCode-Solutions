class Solution(object):
    def findMissingElements(self, nums):
        st=[]
        m,n=min(nums),max(nums)
        for i in range(m,n):
            if i not in nums:
                st.append(i)
        return st
