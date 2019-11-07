import collections
class Solution(object):
    def _findMode(self, root, countDict):
        if root is not None:
            countDict[root.val] += 1
            self._findMode(root.left, countDict)
            self._findMode(root.right, countDict)

    def findMode(self, root):
        if root is None:
            return []
        countDict = collections.defaultdict(int)
        self._findMode(root, countDict)
        maxCount = max(countDict.values())
        return [key for key in countDict if countDict[key] == maxCount]