class Solution:
    def letterCombinations(self, digits):
        lettDic = {'2': ('a', 'b', 'c'), '3': ('d', 'e', 'f'), '4': ('g', 'h', 'i'), '5': ('j', 'k', 'l'),
                   '6': ('m', 'n', 'o'), '7': ('p', 'q', 'r', 's'), '8': ('t', 'u', 'v'), '9': ('w', 'x', 'y', 'z')}
        ressultSet = set()
        for digit in digits:
            if digit in lettDic:
                if len(ressultSet) == 0:
                    for lett in lettDic[digit]:
                        ressultSet.add(lett)
                else:
                    nextResultSet = set()
                    for lett in lettDic[digit]:
                        for res in ressultSet:
                            nextResultSet.add(res + lett)
                    ressultSet = nextResultSet
        return list(ressultSet)


solut = Solution()
s = '203'
print solut.letterCombinations(s)
