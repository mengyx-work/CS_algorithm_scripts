class Solution(object):
    def _max_palindromic_sequence_length(self, chars, left_ptr, right_ptr, matched_count=0):
        cur_left_ptr, cur_right_ptr = left_ptr, right_ptr
        while(cur_left_ptr >= 0 and cur_right_ptr < len(chars)):


    def longestPalindromeSubseq(self, s):
        if len(s) <= 1:
            return len(s)
        max_len = 0
        chars = list(s)
        for i in range(len(chars)-1):
            max_len = max(max_len, self._max_palindromic_sequence_length(chars, i, i+1)
            
