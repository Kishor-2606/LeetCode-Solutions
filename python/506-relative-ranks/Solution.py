class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        cpy=score[:]
        cpy.sort(reverse=True)
        print(cpy)
        dic={}
        ls=[]
        for i in range(len(cpy)):
            if i==0:
                dic[cpy[i]]="Gold Medal"
            elif i==1:
                dic[cpy[i]]="Silver Medal"
            elif i==2:
                dic[cpy[i]]="Bronze Medal"
            else:
                dic[cpy[i]]=str(i+1)
        
        for i in score:
            ls.append(dic[i])

        return ls
        