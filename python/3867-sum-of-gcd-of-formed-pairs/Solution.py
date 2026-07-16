class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        prefixgcd=[]
        for i in range(len(nums)):
            ls.append(max(nums[:i+1]))


        for i,j in zip(nums,ls):
            if i==j:
                prefixgcd.append(i)
                continue
            else:
                mn=min(i,j)
                gcd=0
                for k in range(1,mn+1):
                    if i%k==0 and j%k==0:
                        gcd=k
                prefixgcd.append(gcd)
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
                mn=min(a,b)
                gcd=0
                for k in range(1,mn+1):
                    if a%k==0 and b%k==0:
                        gcd=k
                sm+=gcd
            i+=1
            j-=1

        return sm


        
        

            
