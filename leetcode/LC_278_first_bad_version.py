# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def search_first_bad(self, min_index, max_index):
        if min_index == max_index:
            return min_index

        mid_index = int((max_index - min_index)/2) + min_index
        if isBadVersion(mid_index):
            return self.search_first_bad(min_index, mid_index)
        else:
            return self.search_first_bad(mid_index + 1, max_index)

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.search_first_bad(0, n)

        
