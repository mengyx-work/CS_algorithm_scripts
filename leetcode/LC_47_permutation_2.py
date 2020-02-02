class Solution(object):
    def permuteUnique(self, nums):
        results = []
        nums.sort()
        self.permute_swap(results, 0, len(nums), nums)
        return results

    def permute_swap(self, results, idx, tot, curArr):
        # print('idx: {}, curArr: {}'.format(idx, curArr))
        if idx >= tot:
            results.append(curArr[:])
        tmpCurArr = curArr[:]
        for i in range(idx, tot):
            if i > 0 and tmpCurArr[i-1] == tmpCurArr[i]:
                    continue
            self.swap(tmpCurArr, idx, i)
            self.permute_swap(results, idx+1, tot, tmpCurArr)
            self.swap(tmpCurArr, i, idx)

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp



solut = Solution()

# nums = [1, 1, 1, 3]
# nums = [2,2,1,1]
nums = [0,1,0,0,9]
res = solut.permuteUnique(nums)
ref = [[0,0,0,1,9],[0,0,0,9,1],[0,0,1,0,9],[0,0,1,9,0],[0,0,9,0,1],[0,0,9,1,0],[0,1,0,0,9],[0,1,0,9,0],[0,1,9,0,0],[0,9,0,0,1],[0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],[1,0,9,0,0],[1,9,0,0,0],[9,0,0,0,1],[9,0,0,1,0],[9,0,1,0,0],[9,1,0,0,0]]
print 'the ref: ', len(ref)

## [[1,1,2,2],[1,2,1,2],[1,2,2,1],[2,1,1,2],[2,1,2,1],[2,2,1,1]]
print 'the reults: ', len(res)
