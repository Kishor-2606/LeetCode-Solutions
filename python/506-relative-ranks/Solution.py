class Solution(object):
    def findRelativeRanks(self, score):
        sortedscore=sorted(score,reverse=True)
        rank={}
        for i,val in enumerate(sortedscore):
            if i==0:
                rank[val]="Gold Medal"
            elif i==1:
                rank[val]="Silver Medal"
            elif i==2:
                rank[val]="Bronze Medal"
            else:
                rank[val]=str(i+1)
        return [rank[s] for s in score]