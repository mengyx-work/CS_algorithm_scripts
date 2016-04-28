class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        tmp = nums[0]
        count = 1
        for num in nums[1:]:
            if count == 0:
                tmp = num

            if num == tmp:
                count += 1
            else:
                count -= 1

        return tmp


solut = Solution()
test_1 = [1, 2, 1, 1, 2]
print solut.majorityElement(test_1)

