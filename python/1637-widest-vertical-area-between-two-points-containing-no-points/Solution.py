class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort(key=lambda p: p[0])
        maxWidth=0
        for i in range(1,len(points)):
            maxWidth=max(maxWidth,points[i][0]-points[i-1][0])
        return maxWidth