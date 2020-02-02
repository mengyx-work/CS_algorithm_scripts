class Solution(object):
    def isAlienSorted(self, words, order):
        orderDict = {"": 0}
        for i in range(1, len(order)+1):
            orderDict[order[i-1]] = i

        queue = [list(word) + [""] for word in words]
        while len(queue) > 1:
            nextQueue, idx = [], set()
            for i in range(len(queue)-1):
                if orderDict[queue[i][0]] > orderDict[queue[i+1][0]]:
                    return False
                elif orderDict[queue[i][0]] == orderDict[queue[i+1][0]]:
                    idx.add(i)
                    idx.add(i+1)

            for i in idx:
                if len(queue[i]) == 0:
                    continue
                queue[i].pop(0)
                nextQueue.append(queue[i])
            queue = nextQueue[:]
        return True

sol = Solution()
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
assert sol.isAlienSorted(words, order) == False

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
assert sol.isAlienSorted(words, order) == True


words = ["apple","app"]
order = "abcdefghijklmnopqrstuvwxyz"
assert sol.isAlienSorted(words, order) == False



