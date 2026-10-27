class Solution(object):
    def largestAltitude(self, gain):
        val=0
        mx=0
        for i in gain:
            val+=i
            print(val)
            mx=max(mx,val)
        return mx        