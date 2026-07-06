class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        cnt=0
        ls=[]
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i!=j and intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
                    ls.append(intervals[j])
        for i in intervals:
            if i not in ls:
                cnt+=1
        return cnt