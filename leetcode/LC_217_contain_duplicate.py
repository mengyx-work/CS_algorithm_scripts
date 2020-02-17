# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} k
#     # @return {boolean}
#     def containsNearbyDuplicate(self, nums, k):
#         value_dict = {}
#         for i in range(len(nums)):
#             if nums[i] not in value_dict:
#                 value_dict[nums[i]] = [i]
#             else:
#                 value_dict[nums[i]].append(i)
#
#         for key, index_list in value_dict.iteritems():
#             print index_list
#             if(len(index_list)>1):
#                 min_index = index_list[0]
#                 max_index = index_list[0]
#                 for t in range(1, len(index_list)):
#                     if min_index>index_list[t]:
#                         min_index = index_list[t]
#                     if max_index<index_list[t]:
#                         max_index = index_list[t]
#                 print (max_index-min_index), k
#                 if(max_index-min_index)<=k:
#                     print 'True result'
#                     return True
#
#         return False

class Solution(object):
    def containsDuplicate(self, nums):
        cur = set()
        for num in nums:
            if num not in cur:
                cur.add(num)
            else:
                return True
        return False

solu = Solution()

data = [1, 2, 1, 4, 5, 6, 4]
data = [1, 2, 1]

result = solu.containsNearbyDuplicate(data, 2)
print result
