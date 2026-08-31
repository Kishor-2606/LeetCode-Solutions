class Solution(object):
    def countLargestGroup(self, n):
        freq={}
        cnt=0
        for i in range(1,n+1):
            if i>9:
                copy=i
                xm=0
                while(copy!=0):
                    xm+=copy%10
                    copy=copy/10
                freq[xm]=freq.get(xm,0)+1
            else:
                freq[i]=freq.get(i,0)+1
        mx=0

        for i in freq.values():
            mx=max(mx,i)

        for i in freq.values():
            if i==mx:
                cnt+=1
        return cnt