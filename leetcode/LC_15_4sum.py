class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        res = set([])

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):

                aVal = nums[i]
                bVal = nums[j]

                cIndx = j + 1
                dIndx = len(nums) - 1

                while cIndx<dIndx:
                    if (aVal + bVal + nums[cIndx] + nums[dIndx])==target:
                        unit = [aVal, bVal, nums[cIndx] ,nums[dIndx]]
                        unit.sort()
                        res.add(tuple(unit))
                        cIndx += 1
                        dIndx -= 1
                        continue
                        #print 'diff: %i, res[0]: %i' % (diff, res[0])
                        #print aVal, bVal, nums[cIndx], nums[dIndx]

                    if (aVal + bVal + nums[cIndx] + nums[dIndx])<target:
                        cIndx += 1
                    if (aVal + bVal + nums[cIndx] + nums[dIndx])>target:
                        dIndx -= 1
                       
        return list(res)



solut = Solution()
data = [-1, 2, 1, -4]
data = [0 ,1, 2]
data = [1, 0, -1, 0, -2, 2]
print solut.fourSum(data, 0)
                



