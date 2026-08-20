class Solution(object):
    def calculateScore(self, ins, val):
        score=0
        index=0
        seen=set()
        while(index<len(ins)):
            if index in seen or index<0: return score
            seen.add(index)
            if ins[index]=="jump":
                index=val[index]+index  
            else:
                score+=val[index]
                index+=1
        return score