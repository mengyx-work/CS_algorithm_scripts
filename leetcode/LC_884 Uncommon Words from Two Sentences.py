import collections
class Solution(object):
    def uncommonFromSentences(self, A, B):
        elems = A.split()
        elems.extend(B.split())
        counts = collections.defaultdict(int)
        for elem in elems:
            counts[elem] += 1
        return [key for key in counts if counts[key] == 1]

sol = Solution()
A = "this apple is sweet"
B = "this apple is sour"
print(sol.uncommonFromSentences(A, B))