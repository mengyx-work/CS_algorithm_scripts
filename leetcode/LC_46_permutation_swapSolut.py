class Solution(object):
    def permute(self, nums):
        results = []
        self.permute_swap(results, 0, len(nums), nums)
        return results

    def permute_swap(self, results, idx, tot, curArr):
        # print('idx: {}, curArr: {}'.format(idx, curArr))
        if idx >= tot:
            results.append(curArr[:])
        tmpCurArr = curArr[:]
        for i in range(idx, tot):
            self.swap(tmpCurArr, idx, i)
            self.permute_swap(results, idx+1, tot, tmpCurArr)
            self.swap(tmpCurArr, i, idx)

    def swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp


solut = Solution()
nums = [1, 2, 3]
res = solut.permute(nums)
print 'the reults: ', res
