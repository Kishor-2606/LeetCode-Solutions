class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[]
        for i in str(n):
            arr.append(int(i))
        arr.sort()
        return arr[len(arr)-1]*arr[len(arr)-2]

