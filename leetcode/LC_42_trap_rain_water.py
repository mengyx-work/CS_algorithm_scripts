# class Solution(object):
#     def trap(self, height):
#         left_max_height, right_max_height = [], []
#         cur_max_height = None
#         for i in range(len(height)):
#             if cur_max_height is None:
#                 cur_max_height = height[i]
#             else:
#                 cur_max_height =max(cur_max_height, height[i])
#             left_max_height.append(cur_max_height)
#
#         cur_max_height = None
#         for i in range(len(height)-1, -1, -1):
#             if cur_max_height is None:
#                 cur_max_height = height[i]
#             else:
#                 cur_max_height =max(cur_max_height, height[i])
#             right_max_height.append(cur_max_height)
#         right_max_height.reverse()
#         water_count = 0
#         for i in range(len(height)):
#             max_height = min(left_max_height[i], right_max_height[i])
#             if max_height > height[i]:
#                 water_count += max_height - height[i]
#         return water_count

class Solution(object):
    def trap(self, height):
        left_max, right_max = 0, 0
        left_index, right_index = 0, len(height) - 1
        water_count = 0
        while left_index < right_index:
            left_max = max(left_max, height[left_index])
            right_max = max(right_max, height[right_index])
            if left_max < right_max:
                water_count += left_max - height[left_index]
                left_index += 1
            else:
                water_count += right_max - height[right_index]
                right_index -= 1
        return water_count

sol = Solution()
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [5,2,1,2,1,5]
print sol.trap(height)
