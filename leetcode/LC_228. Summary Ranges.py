# class Solution:
#     # @param {integer[]} nums
#     # @return {string[]}
#     def summaryRanges(self, nums):
#         results = []
#         if len(nums) == 0:
#             return results
#         if len(nums) == 1:
#             result = "%i" % (nums[0])
#             results.append(result)
#             return results
#
#         start = nums[0]
#         end = nums[0]
#
#         for i in xrange(1, len(nums)):
#
#             if nums[i] <= (end + 1):
#                 end = nums[i]
#             else:
#                 if start == end:
#                     result = "%i" % (start)
#                     results.append(result)
#                 else:
#                     result = "%i->%i" % (start, end)
#                     results.append(result)
#
#                 if i == (len(nums) - 1):
#                     result = "%i" % (nums[-1])
#                     results.append(result)
#                     return results
#                 else:
#                     start = nums[i]
#                     end = nums[i]
#
#             if i == (len(nums) - 1):
#                 result = "%i->%i" % (start, end)
#                 results.append(result)
#                 return results

class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if len(nums) == 0:
            return res
        l, r = 0, 0
        while r < len(nums):
            if r < len(nums)-1:
                if nums[r+1] - nums[r] > 1:
                    if l == r:
                        res.append('{}'.format(nums[l]))
                    else:
                        res.append('{}->{}'.format(nums[l], nums[r]))
                    r += 1
                    l = r
                else:
                    r += 1
            else:
                if l == r:
                    res.append('{}'.format(nums[l]))
                else:
                    res.append('{}->{}'.format(nums[l], nums[r]))
                break
        return res



solut = Solution()
data = [0, 5, 9]
print solut.summaryRanges(data)