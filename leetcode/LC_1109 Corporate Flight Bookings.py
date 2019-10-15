# class Solution(object):
#     def corpFlightBookings(self, bookings, n):
#         combinedBookings, rangeDict = [], {}
#         for booking in bookings:
#             window = (booking[0], booking[1])
#             if window not in rangeDict:
#                 rangeDict[window] = 0
#             rangeDict[window] += booking[2]
#         for window in rangeDict:
#             combinedBookings.append((window[0], window[1], rangeDict[window]))
#
#         results = []
#         for i in range(1, n+1):
#             tot = 0
#             for booking in combinedBookings:
#                 if i >= booking[0] and i <= booking[1]:
#                     tot += booking[2]
#             results.append(tot)
#         return results

# import collections
# class Solution(object):
#     def corpFlightBookings(self, bookings, n):
#         countDict = collections.defaultdict(int)
#         for booking in bookings:
#             for i in range(booking[0], booking[1]+1):
#                 countDict[i] += booking[2]
#         return [countDict.get(i, 0) for i in range(1, n+1)]

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        res = [0] * (n+1)
        for booking in bookings:
            res[booking[0]-1] += booking[2]
            res[booking[1]] -= booking[2]
            print(booking, res)
        for i in range(1, n):
            res[i] = res[i] + res[i-1]
        return res[:-1]

sol = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(sol.corpFlightBookings(bookings, n))
