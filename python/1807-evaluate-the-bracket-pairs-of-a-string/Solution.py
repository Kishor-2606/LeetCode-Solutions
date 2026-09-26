class Solution(object):
    def evaluate(self,s,knowledge):
        d={}
        for i in knowledge:
            d[i[0]]=i[1]

        ans=""
        i=0

        while i<len(s):
            if s[i]=='(':
                j=i+1

                while s[j]!=')':
                    j+=1

                word=s[i+1:j]

                if word in d:
                    ans+=d[word]
                else:
                    ans+="?"

                i=j+1
            else:
                ans+=s[i]
                i+=1

        return ans