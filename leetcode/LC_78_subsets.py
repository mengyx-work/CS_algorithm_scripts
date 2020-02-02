class Solution:
    def backtrack(self, results, tmpList, nums, idx):
        curList = tmpList[:]
        results.append(curList)
        for i in range(idx, len(nums)):
            curList.append(nums[i])
            self.backtrack(results, curList, nums, i+1)
            curList.pop()

    def subsets(self, nums):
        results = []
        self.backtrack(results, [], nums, 0)
        return results


'''
different bitwise operation to create the full list
'''
# tot_num_elem = 5
# total = 1 << tot_num_elem # this is the all the possible combinations, represented by bits 1111 for 4 elements
#
# for i in range(total):
#     tmp = []
#     t = i
#     j = 0
#     for j in range(tot_num_elem): # loop through all the bits/elements to assign elements into the bit location
#         if (t==0):
#             break
#
#         if (t & 1):
#             tmp.append(j)
#
#         t = t >> 1
#     print i, tmp




solut = Solution()
nums = [1, 2, 3]
print(solut.subsets(nums))
# nums = [4,1,0]
# print(solut.subsets(nums))
# nums = [1, 2, 2]
# print(solut.subsets(nums))
