class Solution(object):
    def findMissingElements(self, nums):
        st=[]
        n,m=0,100
        for i in nums:
            if n<i:n=i
            if m>i:m=i
        nums=set(nums)
        for i in range(m+1,n):
            if i not in nums:st.append(i)
        return st