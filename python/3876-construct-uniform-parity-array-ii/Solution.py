class Solution(object):
    def uniformArray(self,nums1):
        odd=0
        even=0

        for i in nums1:
            if i%2==0:
                even+=1
            else:
                odd+=1

        if odd==0 or even==0:
            return True

        smallest_odd=float('inf')

        for i in nums1:
            if i%2!=0:
                smallest_odd=min(smallest_odd,i)
        for i in nums1:
            if i%2==0 and i<smallest_odd:
                return False
        return True