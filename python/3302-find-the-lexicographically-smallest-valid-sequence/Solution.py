class Solution(object):
    def validSequence(self, word1, word2):
        n=len(word2)
        last=[-1]*n
        j=n-1

        for i in range(len(word1)-1,-1,-1):
            if j>=0 and word1[i]==word2[j]:
                last[j]=i
                j-=1

        j=cnt=0
        ans=[]

        for i in range(len(word1)):
            if j<n:
                if word1[i]==word2[j] or (cnt==0 and (j==n-1 or i+1<=last[j+1])):
                    if word1[i]!=word2[j]:
                        cnt=1
                    ans.append(i)
                    j+=1

        return ans if j==n else []