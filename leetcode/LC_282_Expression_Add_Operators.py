class Solution(object):
    def addOperators(self, num, target):
        if len(num) == 0:
            return False
        if int(num) == target:
            return True
        for i, char in enumerate(num):


