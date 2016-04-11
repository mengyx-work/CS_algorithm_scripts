class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        res = 0
        if len(nums)==1:
            return nums[0]

        indx = 0
        chose = []
        while True:
            print indx
            if indx>=len(nums):
                return res

            if indx==len(nums)-1:
                res += nums[-1]
                print chose
                return res
            if indx==len(nums)-2:
                if nums[-1]>nums[-2]:
                    res += nums[-1]
                    chose.append(nums[-1])
                    print chose
                    return res
                else:
                    res += nums[-2]
                    chose.append(nums[-2])
                    print chose
                    return res

            cur = nums[indx]- nums[indx+1]
            nex = nums[indx+1] - nums[indx+2]
       
            if cur<nex:
                res += nums[indx+1]
                chose.append(nums[indx+1])
                indx = indx + 3
            else:
                res += nums[indx]
                chose.append(nums[indx])
                indx = indx + 2
            

solut = Solution()
data = [2, 7, 3, 4, 5, 6, 2]
data = [1, 3, 1]
print solut.rob(data)
