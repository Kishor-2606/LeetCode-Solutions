class Solution(object):
    def intersection(self, nums1, nums2):
        st=set()
        nums1=set(nums1)
        nums2=set(nums2)
        for i in nums1:
            if i in nums2:
                st.add(i)
        return list(st)