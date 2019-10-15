# class Solution(object):
#     def numRescueBoats(self, people, limit):
#         people.sort()
#         start, end = 0, len(people) - 1
#         boats = 0
#         while start <= end:
#             if start == end:
#                 return (boats + 1)
#             if people[start] + people[end] > limit:
#                 boats += 1
#                 end -= 1
#             else:
#                 if (end - start) > 2:
#                     start += 1
#                     end -= 1
#                     boats += 1
#                 elif (end - start) == 2:
#                     return (boats + 2)
#                 else:
#                     return (boats + 1)

class Solution(object):
    def numRescueBoats(self, people, limit):
        i, j = 0, len(people) - 1
        boats = 0
        people.sort(reverse=True)
        while i <= j:
            boats += 1
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1
        return boats


sol = Solution()
people = [3,5,3,4]
limit = 5
assert sol.numRescueBoats(people, limit) == 4
people = [3,2,2,1]
limit = 3
assert sol.numRescueBoats(people, limit) == 3

people = [5,1,4,2]
limit = 6
assert sol.numRescueBoats(people, limit) == 2

