class Solution(object):
    def twoSum(self, num, target):
        dic={}
        for i in range(len(num)):
            val=target-num[i]
            if val in dic:return [dic[val]+1,i+1]
            else:dic[num[i]]=i
            