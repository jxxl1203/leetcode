class Solution(object):
    def countBits(self, num):
        res = [0]
        for i in range(1, num+1):
            tmp = res[i>>1] + (i&1)
            res.append(tmp)
        return res

