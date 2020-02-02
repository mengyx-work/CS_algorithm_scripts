#
#
# def max_area_histogram(histogram):
#     # This function calulates maximum
#     # rectangular area under given
#     # histogram with n bars
#
#     # Create an empty stack. The stack
#     # holds indexes of histogram[] list.
#     # The bars stored in the stack are
#     # always in increasing order of
#     # their heights.
#     stack = list()
#
#     max_area = 0  # Initialize max area
#
#     # Run through all bars of
#     # given histogram
#     index = 0
#     while index < len(histogram):
#
#         # If this bar is higher
#         # than the bar on top
#         # stack, push it to stack
#
#         if (not stack) or (histogram[stack[-1]] <= histogram[index]):
#             stack.append(index)
#             index += 1
#
#         # If this bar is lower than top of stack,
#         # then calculate area of rectangle with
#         # stack top as the smallest (or minimum
#         # height) bar.'i' is 'right index' for
#         # the top and element before top in stack
#         # is 'left index'
#         else:
#             # pop the top
#             top_of_stack = stack.pop()
#
#             # Calculate the area with
#             # histogram[top_of_stack] stack
#             # as smallest bar
#             area = (histogram[top_of_stack] *
#                     ((index - stack[-1] - 1)
#                      if stack else index))
#             print(area, top_of_stack, index, stack)
#
#             # update max area, if needed
#             max_area = max(max_area, area)
#
#             # Now pop the remaining bars from
#     # stack and calculate area with
#     # every popped bar as the smallest bar
#     while stack:
#         # pop the top
#         top_of_stack = stack.pop()
#
#         # Calculate the area with
#         # histogram[top_of_stack]
#         # stack as smallest bar
#         area = (histogram[top_of_stack] *
#                 ((index - stack[-1] - 1)
#                  if stack else index))
#         print('outside', area, top_of_stack, index, stack)
#         # update max area, if needed
#         max_area = max(max_area, area)
#
#         # Return maximum area under
#     # the given histogram
#     return max_area


class Solution(object):
    def largestRectangleArea(self, heights):
        maxS, stack = 0, []
        idx = 0
        while idx < len(heights):
            if len(stack) == 0 or heights[stack[-1]] < heights[idx]:
                stack.append(idx)
                idx += 1
            else:
                top_idx = stack.pop()
                left_end = stack[-1] if stack else -1
                area = heights[top_idx] * (idx - left_end - 1)
                maxS = max(maxS, area)

        while stack:
            top_idx = stack.pop()
            left_end = stack[-1] if stack else -1
            area = heights[top_idx] * (idx - left_end - 1)
            maxS = max(maxS, area)

        return maxS

sol = Solution()
hist = [6, 2, 5, 4, 5, 1, 6]
# hist = [1, 2, 3, 4]
print("Maximum area is",
      sol.largestRectangleArea(hist))
