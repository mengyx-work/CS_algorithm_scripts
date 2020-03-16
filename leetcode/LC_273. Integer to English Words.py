class Solution(object):
    oneToNineteen = ('One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve '
                    'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen').split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    units = ['Billion', 'Million', 'Thousand']

    def numberToWords(self, num):
        if num == 0:
            return "Zero"
        if num < 20:
            return self.oneToNineteen[num-1]
        if num < 100:
            cur = self.tens[(num/10-2)]
            if num % 10 != 0:
                cur += ' ' + self.oneToNineteen[num % 10 - 1]
            return cur
        if num < 1000:
            cur = self.oneToNineteen[num/100-1] + " Hundred"
            if num % 100 != 0:
                cur += ' ' + self.numberToWords(num % 100)
            return cur

        res, i = "", 0
        while i < 3:
            unit = 1000**(3-i)
            if num / unit > 0:
                cur = self.numberToWords(num/unit) + ' ' + self.units[i]
                if num % unit != 0:
                    cur += ' ' + self.numberToWords(num%unit)
                res += cur
                return res
            i += 1

sol = Solution()
# print(sol.numberToWords(1594))
print(sol.numberToWords(1234567))


