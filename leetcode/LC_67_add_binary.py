# class Solution:
#     def addBinary(self, a, b):
#         aList = [int(x) for x in a]
#         bList = [int(x) for x in b]
#
#         if len(aList)>=len(bList):
#             bList = [0]*( len(aList) - len(bList)) + bList
#         else:
#             aList = [0]*( len(bList) - len(aList)) + aList
#
#         residual = 0
#         result = []
#         for a, b in zip(reversed(aList), reversed(bList)):
#             if (a+b+residual)>=2:
#                 result.append(a+b+residual-2)
#                 residual = 1
#             else:
#                 result.append(a+b+residual)
#                 residual = 0
#
#         if residual==1:
#             result.append(1)
#
#         strNum = "".join(str(x) for x in reversed(result))
#
#         return strNum

# class Solution(object):
#     def addBinary(self, a, b):
#         res = []
#         cur = 0
#         i, j = 0, 0
#         a = a[::-1]
#         b = b[::-1]
#         # print(a, b)
#         while i < len(a) or j < len(b):
#             if i < len(a):
#                 cur += int(a[i])
#             if j < len(b):
#                 cur += int(b[j])
#             # print(i, j, cur)
#             if cur >= 2:
#                 res.append(str(cur - 2))
#                 cur = 1
#             else:
#                 res.append(str(cur))
#                 cur = 0
#             i += 1
#             j += 1
#         if cur == 1:
#             res.append(str(cur))
#         return ''.join(reversed(res))

class Solution(object):
    def addBinary(self, a, b):
        res = []
        cur = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            if i >= 0:
                cur += int(a[i])
            if j >= 0:
                cur += int(b[j])
            res.append(str(cur%2))
            cur = cur / 2
            j -= 1
            i -= 1
        if cur > 0:
            res.append(str(cur))
        return ''.join(reversed(res))


solut = Solution()
# print solut.addBinary("11", "1")

print solut.addBinary("1010", "1011")


