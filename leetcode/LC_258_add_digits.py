class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            new_num_list = [int(elem) for elem in str(num)]
            new_num = new_num_list.sum()
