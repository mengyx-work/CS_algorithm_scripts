from collections import defaultdict
class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        arrays, cnts = [], defaultdict(int)
        for i in range(len(values)):
            arrays.append((values[i], labels[i]))
        arrays.sort(key=lambda x: x[0], reverse=True)
        res = 0
        for v, l in arrays:
            if num_wanted == 0:
                break
            if cnts[l] < use_limit:
                res += v
                cnts[l] += 1
                num_wanted -= 1
        return res

sol = Solution()
values = [5,4,3,2,1]
labels = [1,1,2,2,3]
assert sol.largestValsFromLabels(values, labels, 3, 1) == 9

values = [5,4,3,2,1]
labels = [1,3,3,3,2]
assert sol.largestValsFromLabels(values, labels, 3, 2) == 12

values = [9,8,8,7,6]
labels = [0,0,0,1,1]
assert sol.largestValsFromLabels(values, labels, 3, 1) == 16

values = [9,8,8,7,6]
labels = [0,0,0,1,1]
assert sol.largestValsFromLabels(values, labels, 3, 2) == 24