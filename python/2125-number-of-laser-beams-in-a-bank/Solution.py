class Solution(object):
    def numberOfBeams(self, bank):
        sm=0
        last=0
        for i in bank:
            cnt=0
            for j in i:
                if j=='1':cnt+=1
            if cnt!=0:
                sm+=last*cnt
                last=cnt
        return sm
        