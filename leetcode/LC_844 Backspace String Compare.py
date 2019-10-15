class Solution(object):
    def _typeContent(self, S):
        ctnt = []
        for char in S:
            if char == '#':
                if len(ctnt) > 0:
                    ctnt.pop()
            else:
                ctnt.append(char)
        return ctnt

    def backspaceCompare(self, S, T):
        typedS = self._typeContent(S)
        typedT = self._typeContent(T)
        print(typedS, typedT)
        return typedS == typedT

sol = Solution()
S = "ab#c"
T = "ad#c"
assert sol.backspaceCompare(S, T) == True
S = "ab##"
T = "c#d#"
assert sol.backspaceCompare(S, T) == True
