# class Solution(object):
#     def addStrings(self, num1, num2):
# 	num1 = list(num1)
#         num2 = list(num2)
#         if len(num1) > len(num2):
#             longStr = num1
#             shrtStr = num2
#         else:
#             longStr = num2
#             shrtStr = num1
#         offset = len(longStr) - len(shrtStr)
#         newSum = []
#         extra = 0
#         for i in range(len(shrtStr) - 1, -1, -1):
#             tmpSum = int(longStr[offset + i]) + int(shrtStr[i]) + extra
#             if tmpSum > 9:
#                 tmpSum = tmpSum - 10
#                 newSum.append(str(tmpSum))
#                 extra = 1
#             else:
#                 newSum.append(str(tmpSum))
#                 extra = 0
#
#         for i in range(offset - 1, -1, -1):
#             tmpSum = int(longStr[i]) + extra
#             if tmpSum > 9:
#                 tmpSum = tmpSum - 10
#                 newSum.append(str(tmpSum))
#                 extra = 1
#             else:
#                 newSum.append(str(tmpSum))
#                 extra = 0
#
#         if extra == 1:
#             newSum.append(str(1))
#
#         return ''.join(newSum[::-1])

class Solution(object):
    def addStrings(self, num1, num2):
        res, cur = [], 0
        i, j = len(num1)-1, len(num2)-1
        while i >= 0 or j >= 0:
            if i >= 0:
                cur += int(num1[i])
            if j >= 0:
                cur += int(num2[j])
            res.append(str(cur % 10))
            cur = cur / 10
            i -= 1
            j -= 1
        if cur > 0:
            res.append(str(cur))
        print(res)
        return ''.join(reversed(res))

sol = Solution()
assert sol.addStrings('1234', '23') == '1257'
assert sol.addStrings('999', '99') == '1098'

            
        
