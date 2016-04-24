'''
1. use bit to indicate whether a letter exists
2. sor the word list by word length, so the maximum computation O(n^2)

a.
ASCII value for character: 
convert ASCII value into character 
ord('a') ## 97
chr(97) ## 'a'
convert character into ASCII value
ord('z') ## 122. 

b.
convert string to list
list('abc') ## ['a', 'b', 'c']

convert list into set set(['a', 'a', 'b'])
'''

class Solution(object):
    def word2bits(self, word):
        bits = ''
        char_set = set(list(word))
        for asc_value in range(97, 123):
            if chr(asc_value) in char_set:
                bits += '1'
            else:
                bits += '0'
        #return bits
        return int(bits, 2)

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if len(words) == 0 or len(words) == 1:
            return 0

        #sorted_words = words[:]
        #sorted_words.sort(key = len, reverse=True)
        words_in_bits = [self.word2bits(word) for word in words]
        maxLen = 0
        for i in range(len(words_in_bits) -1):
            word_A = words_in_bits[i]
            for j in range(i, len(words_in_bits)):
                word_B = words_in_bits[j]
                if word_A & word_B == 0:
                    if maxLen < len(words[i]) * len(words[j]):
                        maxLen = len(words[i]) * len(words[j]) 
        return maxLen



solut = Solution()
#print solut.word2bits('hahab')
test_a = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print solut.maxProduct(test_a)
test_b = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
print solut.maxProduct(test_b)
test_c = ["a", "aa", "aaa", "aaaa"]
print solut.maxProduct(test_c)
    
