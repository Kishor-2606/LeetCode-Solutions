class Solution(object):

    def gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        prefixgcd=[]
        mx = 0
        for x in nums:
            mx=max(mx, x)
            ls.append(mx)
        for i,j in zip(nums,ls):
            if i==j:
                prefixgcd.append(i)
            else:
                g=self.gcd(i,j)
                prefixgcd.append(g)
        prefixgcd.sort()
        mid=0
        if len(prefixgcd)%2!=0:
            mid=len(prefixgcd)//2
            prefixgcd.pop(mid)

        i=0
        j=len(prefixgcd)-1
        sm=0
        while(i<j):
            a,b=prefixgcd[i],prefixgcd[j]
            if a==b:
                sm+=a
            else:
                g=self.gcd(a,b)
                sm+=g
            i+=1
            j-=1

        return sm


        
        

            
