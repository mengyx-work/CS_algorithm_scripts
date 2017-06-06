class Solution(object):
    def groupAnagrams(self, strs):
        anagram_dict = {}
        for string in strs:
            num_str = [ord(elem) for elem in list(string)]
            num_str.sort()
            num_str = tuple(num_str)
            if num_str not in anagram_dict:
                anagram_dict[num_str] = []
            anagram_dict[num_str].append(string)
        return [array for array in anagram_dict.values()]
sol =Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print sol.groupAnagrams(strs)

