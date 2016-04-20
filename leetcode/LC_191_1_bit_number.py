class Solution(object):
    def cal_bits(self, n, denom):
        count = 0
        while n != 0:
            num = n % denom
            if num == 1:
                count += 1
            n = n / denom

        return count

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.cal_bits(n, denom= 2)
