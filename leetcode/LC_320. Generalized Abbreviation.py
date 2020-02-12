class Solution(object):
    def generateAbbreviations(self, word):
        results = []
        self.dsf(results, list(word), 0)
        return results

    def combineNums(self, s):
        stack = []
        for char in s:
            if char.isdigit() and len(stack)>0 and stack[-1].isdigit():
                preNum = int(stack.pop())
                num = int(char) + preNum
                stack.append(str(num))
            else:
                stack.append(char)
        return stack
        # return ''.join(stack)

    def dsf(self, results, curRes, idx):
        results.append(''.join(self.combineNums(curRes)))
        tmpRes = curRes[:]
        # print(idx, curRes)
        for i in range(idx, len(curRes)):
            tmp = tmpRes[i]
            tmpRes[i] = '1'
            self.dsf(results, tmpRes, i+1)
            tmpRes[i] = tmp


sol = Solution()
word = 'word'
res = sol.generateAbbreviations(word)
ref = set(["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"])
assert ref == set(res)