class Solution:
    '''
    def permute(self, nums):
        if len(nums)==1:
            return [[nums[0]]]
        stack = []
        res = []
        for num in nums:
            stack.append([num])
        while stack:
            v = stack.pop()
            if len(v)==len(nums): res.append(v)
            else:
                for num in nums:
                    if num not in v:
                        tmp = v[:]
                        tmp.append(num)
                        stack.append(tmp)
        return res
    '''

solut = Solution()
#nums = []
#nums = [1, 2]
#nums = [4,1,0, 3]
nums = [1, 2, 3]
#nums = [1, 1, 2, 2, 3]
print solut.permute(nums) 
