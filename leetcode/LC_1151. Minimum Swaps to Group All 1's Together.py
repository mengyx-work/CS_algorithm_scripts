class Solution(object):
    def minSwaps(self, data):
        tot = sum(data)
        res = tot
        j, cur = 0, 0
        while j < len(data):
            cur += data[j]
            if (j+1) > tot:
                cur -= data[j - tot]
            res = min(res, tot - cur)
            j += 1
        return res
