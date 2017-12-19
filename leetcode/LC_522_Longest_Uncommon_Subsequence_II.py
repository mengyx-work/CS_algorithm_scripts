class Solution(object):
    def findLUSlength(self, strs):
        len_map = {}
        for single_str in strs:
            single_len = len(single_str)
            if single_len  not in len_map:
                len_map[single_len] = []
            len_map[single_len].append(single_str)
        len_pairs = len_map.items()
        len_pairs.sort(key=lambda x : x[0], reverse=True)
        for key, value in len_pairs:
            if if len(value) == 1:
                return key
            else:


