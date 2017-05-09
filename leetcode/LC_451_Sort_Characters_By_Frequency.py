class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        result = ''
        for char, count in sorted_items:
            result += count*char
        return result


sol = Solution()
input = 'cccaaa'
print sol.frequencySort(input)
input = 'Bbaa'
print sol.frequencySort(input)



       
