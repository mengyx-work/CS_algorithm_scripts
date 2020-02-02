
class Solution(object):
    def removeKdigits(self, num, k):
        s = []
        for i in range(len(num)):
            while len(s) > 0 and int(s[-1]) > int(num[i]) and k > 0:
                s.pop()
                k -= 1
            s.append(num[i])
        # print(s)
        while k > 0 and len(s) > 0:
            s.pop()
            k -= 1
        while len(s) > 0 and s[0] == '0':
            s.pop(0)
        if len(s) == 0:
            return '0'
        return ''.join(s)


sol = Solution()
num = '112'
k = 1
print(sol.removeKdigits(num, k))

# num = '1432219'
# k = 3
# assert sol.removeKdigits(num, k) == '1219'
#
# num = '10200'
# k = 1
# assert sol.removeKdigits(num, k) == '200'