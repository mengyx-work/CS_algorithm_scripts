'''
1. good solution by keeping tracks of the repeative pattterns:
    100, 101, 110, 111, is similar to 00, 01, 10, 11
'''
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # sheating way with python
        bitList = []
        for i in range(num+1):
            bitString = "{0:b}".format(i)
            bitNum = sum(map(int, list(bitString)))
            bitList.append(bitNum)

        return bitList


solut = Solution()
print solut.countBits(5)


