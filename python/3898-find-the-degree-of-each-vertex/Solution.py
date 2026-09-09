class Solution(object):
    def findDegrees(self, matrix):
        ls=[]
        for i in matrix:
            cnt=0
            for j in i:
                if j==1:
                    cnt+=1
            ls.append(cnt)
        return ls