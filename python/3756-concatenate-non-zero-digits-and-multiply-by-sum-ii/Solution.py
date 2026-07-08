MOD=1000000007
MAX=100001
p=[1]*MAX
for i in range(1,MAX):
    p[i]=(p[i-1]*10)%MOD

class Solution:
    def sumAndMultiply(self,s,queries):
        n=len(s)
        A=[0]*(n+1)
        B=[0]*(n+1)
        ln=[0]*(n+1)

        for i,c in enumerate(s):
            d=ord(c)-48
            A[i+1]=A[i]+d
            if d:
                B[i+1]=(B[i]*10+d)%MOD
                ln[i+1]=ln[i]+1
            else:
                B[i+1]=B[i]
                ln[i+1]=ln[i]

        ans=[]
        for l,r in queries:
            r+=1
            x=(B[r]-B[l]*p[ln[r]-ln[l]])%MOD
            ans.append((x*(A[r]-A[l]))%MOD)
        return ans