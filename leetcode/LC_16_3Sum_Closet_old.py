class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = [2**30, (0, 0, 0)]
        for i in range(len(nums)-2):
            aVal = nums[i]
            bIndx = i + 1
            cIndx = len(nums) - 1

            while bIndx<cIndx:
                diff = aVal + nums[bIndx] + nums[cIndx] - target
                print 'diff: %i, res[0]: %i' % (diff, res[0])
                print aVal, nums[bIndx], nums[cIndx]
                if abs(diff)<=res[0]:
                    res[1] = (aVal, nums[bIndx], nums[cIndx])
                    res[0] = abs(diff)
                if diff>0:
                    cIndx -= 1
                elif diff<0:
                    bIndx += 1
                else:
                    return target
        
        return sum(res[1])



solut = Solution()
data = [-1, 2, 1, -4]
data = [0 ,1, 2]
data = [1 ,1, 1, 0]
print solut.threeSumClosest(data, -100)
                


