# class Solution:
#     # @param {string} num1
#     # @param {string} num2
#     # @return {string}
#     def multiply(self, num1, num2):
#         res = '0'
#         for digit_offset, one_digit in enumerate(num1[::-1]):
#             tmpRes = self.multipleNum(digit_offset, one_digit, num2)
#             res = self.addNum(tmpRes, res)
#         return res
#
#     def addNum(self, num1, num2):
#         if len(num1)<=len(num2):
#             length = len(num2)
#             num1 = '0'*(len(num2)-len(num1)) + num1
#         else:
#             length = len(num1)
#             num2 = '0'*(len(num1)-len(num2)) + num2
#
#         res = []
#         tmpOffset = 0
#         for i in range(-1, -(length+1), -1):
#             tmpSum = int(num1[i]) + int(num2[i]) + tmpOffset
#             res.append(str(tmpSum%10))
#             tmpOffset = (tmpSum - tmpSum%10)/10
#         if tmpOffset != 0:
#             res.append(str(tmpOffset))
#         return ''.join(res[::-1])
#
#     def multipleNum(self, digit_offset, one_digit, num2):
#         if int(one_digit)==0 or len(num2)==1 and int(num2)==0:
#             return '0'
#
#         res = []
#         if digit_offset>0:
#             res = ['0'*digit_offset]
#         tmpOffset = 0
#
#         for digit in num2[::-1]:
#             tmpRes = int(digit)*int(one_digit) + tmpOffset
#             digit = tmpRes%10
#             tmpOffset = (tmpRes - digit)/10
#             res.append(str(digit))
#
#         if tmpOffset!=0:
#             res.append(str(tmpOffset))
#
#         return ''.join(res[::-1])

# class Solution(object):
#     def multiply(self, num1, num2):
#         res, cur = [], 0
#         tot = len(num1) + len(num2) - 1
#         num1, num2 = num1[::-1], num2[::-1]
#         for k in range(1, tot+1):
#             for i in range(1, len(num1)+1):
#                 j = k + 1 - i
#                 if j > len(num2) or j <= 0:
#                     continue
#                 # print(i, j, cur)
#                 cur += int(num1[i-1]) * int(num2[j-1])
#             # print('k: ', k, cur)
#             res.append(str(cur % 10))
#             cur = cur / 10
#         if cur > 0:
#             res.append(str(cur))
#         while len(res) > 1 and res[-1] == '0':
#                 res = res[:-1]
#         # print(res)
#         return ''.join(reversed(res))

class Solution(object):
    def multiply(self, num1, num2):
        res, cur = [], 0
        tot = len(num1) + len(num2) - 1
        len1, len2 = len(num1), len(num2)
        for k in range(1, tot+1):
            for i in range(len1, 0, -1):
                ## len1 - i + 1 + len2 - j + 1 = k + 1
                j = len1 + len2 + 1 - i - k
                if j > len(num2) or j <= 0:
                    continue
                # print(i, j, cur)
                cur += int(num1[i-1]) * int(num2[j-1])
            # print('k: ', k, cur)
            res.append(str(cur % 10))
            cur = cur / 10
        if cur > 0:
            res.append(str(cur))
        while len(res) > 1 and res[-1] == '0':
                res = res[:-1]
        # print(res)
        return ''.join(reversed(res))

solut = Solution()
# print solut.multiply('0', '79')
print solut.multiply('123', '456')
