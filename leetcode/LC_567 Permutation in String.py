#         countDict, counts = {}, 0
#         inSearch = False
#         for elem in s1:
#             if elem not in countDict:
#                 countDict[elem] = 0
#             countDict[elem] += 1
#         start, totCounts = 0, len(countDict)
#         currentDict = countDict.copy()
#         for i in range(len(s2)):
#             elem = s2[i]
#             if inSearch and elem not in currentDict:
#                 currentDict = countDict.copy()
#                 inSearch = False
#                 counts = 0
#                 continue
#             elif elem in currentDict:
#                 if not inSearch:
#                     start = i
#                     inSearch = True
#                 currentDict[elem] -= 1
#                 if currentDict[elem] == 0:
#                     counts += 1
#                 while counts == totCounts:
#                     if all([currentDict[key] == 0 for key in currentDict]):
#                         return True
#                     currentDict[s2[start]] += 1
#                     if currentDict[s2[start]] > 0:
#                         counts -= 1
#                     start += 1
#         return False

import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        dict1 = collections.defaultdict(int)
        dict2 = collections.defaultdict(int)
        for elem in s1:
            dict1[elem] += 1
        for elem in s2[:len(s1)]:
            dict2[elem] += 1
        i, j = 0, len(s1)

        while j < len(s2):
            if dict1 == dict2:
                return True
            dict2[s2[j]] = dict2.get(s2[j], 0) + 1
            dict2[s2[i]] -= 1
            if dict2[s2[i]] < 1:
                _ = dict2.pop(s2[i])
            i += 1
            j += 1
        return False


sol = Solution()
s1 = "ab"
s2 = "eidbaooo"
assert sol.checkInclusion(s1, s2) == True

s1= "ab"
s2 = "eidboaoo"
assert sol.checkInclusion(s1, s2) == False

s1 = "adc"
s2 = "dcda"
assert sol.checkInclusion(s1, s2) == True

s1 = "abcdxabcde"
s2 = "abcdeabcdx"
assert sol.checkInclusion(s1, s2) == True
