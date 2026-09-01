class Solution(object):
    def frequencySort(self, s):
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        empty=""
        for key,value in reversed(sorted(freq.items(), key=lambda item: item[1])):
            empty+=str(key*value)
        return empty
