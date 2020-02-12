# class Solution(object):
#     def groupAnagrams(self, strs):
#         anagram_dict = {}
#         for string in strs:
#             num_str = [ord(elem) for elem in list(string)]
#             num_str.sort()
#             num_str = tuple(num_str)
#             if num_str not in anagram_dict:
#                 anagram_dict[num_str] = []
#             anagram_dict[num_str].append(string)
#         return [array for array in anagram_dict.values()]

from collections import defaultdict
class Solution(object):
    def convert2Dict(self, arr):
        dic = defaultdict(int)
        for s in arr:
            dic[s] += 1
        return tuple([(key, dic[key]) for key in sorted(dic.keys())])

    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        for arr in strs:
            key = self.convert2Dict(arr)
            dic[key].append(arr)
        return [dic[key] for key in dic]

sol =Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print sol.groupAnagrams(strs)

