from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        cnts = {"U": 0, "D": 0,  "L": 0, "R": 0}
        for s in moves:
            cnts[s] += 1
        if cnts["U"] != cnts["D"]:
            return False
        if cnts["L"] != cnts['R']:
            return False
        return True