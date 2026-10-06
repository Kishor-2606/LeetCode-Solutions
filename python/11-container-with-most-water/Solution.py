class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        ans=0
        while(l<r):
            water=(r-l)*(min(height[l],height[r]))
            ans=max(ans,water)
            if height[l]<height[r]:l+=1
            else:r=r-1
        return ans