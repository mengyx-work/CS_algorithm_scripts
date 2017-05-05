class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
	cur_r, cur_c = len(nums), len(nums[0])
        if cur_r * cur_c != r * c:
            return nums

        new_nums = []
        cur_row = []
        for row in nums:
            for elem in row:
                print elem
                if len(cur_row) < c:
                    cur_row.append(elem)
                else:
                    new_nums.append(cur_row)
                    cur_row = []
                    cur_row.append(elem)

        new_nums.append(cur_row)

        return new_nums



sol = Solution()
nums = [[1,2],
         [3,4]]

expected = [[1,2,3,4]]
#print sol.matrixReshape(nums, 4, 1)
assert expected == sol.matrixReshape(nums, 1, 4)
expected = [[1],[2],[3],[4]]
assert expected == sol.matrixReshape(nums, 4, 1)
