class Solution(object):
    def garbageCollection(self, garbage, travel):
        g=0
        p=0
        m=0
        val=0
        prefix_sum=[0]
        positions=[0]*3
        for i in travel:
            val+=i
            prefix_sum.append(val)
        for i in range(len(garbage)):
            for letter in garbage[i]:
                if letter=='G':
                    g=g+1
                    positions[0]=i
                if letter=='P':
                    p=p+1
                    positions[1]=i
                if letter=='M':
                    m=m+1
                    positions[2]=i
        add=0
        for i in positions:
            add+=prefix_sum[i]
        add+=m+g+p
        return add