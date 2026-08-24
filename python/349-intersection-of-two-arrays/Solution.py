class Solution(object):
    def intersection(self, nums1, nums2):
        st=set()
        for i in nums1:
            if i in nums2:
                st.add(i)
        return list(st)