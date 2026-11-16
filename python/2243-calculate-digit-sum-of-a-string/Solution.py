class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            nxt = []
            for i in range(0, len(s), k):
                nxt.append(str(sum(int(c) for c in s[i:i + k])))
            s = "".join(nxt)
        return s