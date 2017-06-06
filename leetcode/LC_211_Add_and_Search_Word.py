class WordDictionary(object):
    def __init__(self):
        self.word_dict = {}

    def addWord(self, word):
        cur_dict = self.word_dict
        for char in list(word) + ["~"]:
            if char not in cur_dict:
                cur_dict[char] = {}
            cur_dict = cur_dict[char]

    def _search_full_space(self, cur_dict, word):
        for key in cur_dict:
            if self._found_match(cur_dict[key], word):
                return True
        return False
    
    def _found_match(self, cur_dict, word):
        for i, char in enumerate(word):
            if char == '.':
                return self._search_full_space(cur_dict, word[i+1:])
            if char not in cur_dict:
                return False
            else:
                cur_dict = cur_dict[char]
        return True

    def search(self, word):
        cur_dict = self.word_dict
        word = list(word) + ["~"]
        return self._found_match(cur_dict, word)

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
print obj.search('pad')
print obj.search('bad')
print obj.search('.ad')
print obj.search('b..')
