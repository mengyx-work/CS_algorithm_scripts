class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        i1, i2, i3 = 0, 0, 0
        res = []
        while i1 < len(arr1) and i2 < len(arr2) and i3 < len(arr3):
            cur_min = min([arr1[i1], arr2[i2], arr3[i3]])
            if cur_min == arr1[i1] and cur_min == arr2[i2] and cur_min == arr3[i3]:
                res.append(cur_min)
            print(i1, i2, i3, cur_min)
            if cur_min == arr1[i1] and i1 < len(arr1):
                i1 += 1
            if cur_min == arr2[i2] and i1 < len(arr2):
                i2 += 1
            if cur_min == arr3[i3] and i1 < len(arr3):
                i3 += 1
        return res

sol = Solution()
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
# print(sol.arraysIntersection(arr1, arr2, arr3))
assert sol.arraysIntersection(arr1, arr2, arr3) == [1, 5]