# class Solution:
#     # @param {string} s
#     # @return {integer}
#     def lengthOfLongestSubstring(self, s):
#         charList = list(s)
#         startIndex, maxLen = 0, 0
#         charDict = {}
#         print charList
#         for i in range(len(charList)):
#             if charList[i] not in charDict:
#                 charDict[charList[i]] = i
#
#             else:
#                 print 'index %i is repeated, previous index: %i' % (i, charDict[charList[i]])
#                 if startIndex <= charDict[charList[i]]:
#                     startIndex = charDict[charList[i]]+1
#                     print 'change startIndex to: %i' % (startIndex)
#
#                 ##the index for repeated index is always up to date
#                 charDict[charList[i]] = i
#
#             print ('value i: %i, startIndex: %i') % (i, startIndex)
#             length = i - startIndex + 1
#             maxLen = max(maxLen, length)
#
#         return maxLen


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        maxLen = 1
        start, end = 0, 0
        charDict = {}
        for index in range(len(s)):
            char = s[index]
            if char in charDict and charDict[char] >= start:
                start = charDict[char] + 1
            else:
                end = index
                maxLen = max(maxLen, (end - start + 1))
            charDict[char] = index
        return maxLen

solut = Solution()
s = "abcabcbb"
print(solut.lengthOfLongestSubstring(s))
# data = 'qwnfenpglqdq'
# print solut.lengthOfLongestSubstring(data)
