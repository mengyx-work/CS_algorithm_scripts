# class Solution:
#     # @param {integer[]} height
#     # @return {integer}
#
#     def maxArea(self, height):
#         if len(height)<=1:
#             return 0
#         if len(height)==2:
#             return min(height[0], height[1])
#
#         i = 0
#         j = len(height) - 1
#
#         water = 0
#         final_i = i
#         final_j = j
#
#         while j>i:
#             if water<(j-i)*min(height[i], height[j]):
#                 water = (j-i)*min(height[i], height[j])
#                 final_i = i
#                 final_j = j
#
#             if height[i]> height[j]:
#                 j -= 1
#             else:
#                 i += 1
#
#         print 'i, j: ', final_i, final_j
#         return water
#
#     ########################################
#
#     def heightFirst_maxArea(self, height):
#         if len(height)<=1:
#             return 0
#         if len(height)==2:
#             return min(height[0], height[1])
#
#         height = zip(height, range(len(height)))
#         height.sort(key=lambda elem: elem[0], reverse=True)
#
#         sideLong = height[1][1]
#         leftEnd = min(height[0][1], height[1][1])
#         rightEnd = max(height[0][1], height[1][1])
#         print height
#         for elem in height[2:]:
#             #print sideLong, leftEnd, rightEnd
#             #print 'elem: ', elem[0], elem[1]
#             if elem[1]<leftEnd and (elem[0]*(rightEnd-elem[1]))>(sideLong*(rightEnd-leftEnd)):
#                 sideLong = elem[0]
#                 leftEnd = elem[1]
#                 continue
#             if elem[1]>rightEnd and (elem[0]*(elem[1]-leftEnd))>(sideLong*(rightEnd-leftEnd)):
#                 sideLong = elem[0]
#                 rightEnd = elem[1]
#                 continue
#
#         print 'long: ', sideLong, 'i, j: ', leftEnd, rightEnd
#         return sideLong*(rightEnd-leftEnd)
               

class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height)-1
        res = 0
        while i < j:
            res = max(res, min(height[i], height[j])*(j-i))
            if height[i] < height[j]:
                 i += 1
            else:
                j -= 1
        return res

solut = Solution()
data = [76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191]
# print solut.heightFirst_maxArea(data)
print solut.maxArea(data)
