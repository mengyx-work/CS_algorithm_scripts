class Solution(object):
    def maxLength(self, arr):
        setArr = []
        for elem in arr:
            oneSet = set(elem)
            if len(oneSet) == len(elem):
                setArr.append(oneSet)
        if len(setArr) == 0:
            return 0
        curSetArr = []
        for oneSet in setArr:
            nextSetArr = curSetArr[:]
            for otherSet in curSetArr:
                newSet = oneSet | otherSet
                if len(newSet) == (len(oneSet) + len(otherSet)):
                    nextSetArr.append(newSet)
            nextSetArr.append(oneSet)
            curSetArr = nextSetArr
        return max([len(oneSet) for oneSet in curSetArr])

sol = Solution()
arr = ["cha","r","act","ers"]
assert sol.maxLength(arr) == 6
arr = ["yy","bkhwmpbiisbldzknpm"]
assert sol.maxLength(arr) == 0

