import heapq


# class Solution(object):
#     def nthSuperUglyNumber(self, n, primes):
#         heap = primes[:]
#         # heap.append(1)
#         # heapq.heapify(heap)
#         counter, curVal = 0, 1
#         while True:
#             if curVal in heap:
#                 counter += 1
#                 # print(curVal, heap)
#             else:
#                 curMin = heap[0]
#                 for prime in primes:
#                     if curVal % prime == 0 and curVal/prime in heap:
#                         counter += 1
#                         if curVal > curMin * curMin:
#                             heapq.heapreplace(heap, curVal)
#                         else:
#                             heapq.heappush(heap, curVal)
#                         # print(curVal, heap)
#                         break
#             if counter == n:
#                 return curVal
#             curVal += 1

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        if n == 1:
            return 1
        T, idxArr = len(primes), [0 for _ in range(len(primes))]
        res = [1]
        for i in range(n-1):
            curMin = float('inf')
            for i in range(T):
                if res[idxArr[i]]*primes[i] == res[-1]:
                    idxArr[i] += 1
                curMin = min(curMin, res[idxArr[i]]*primes[i])

            # ## remove the duplicates
            # for i in range(T):
            #     if res[idxArr[i]]*primes[i] == curMin:
            #         idxArr[i] += 1

            res.append(curMin)
        return res[-1]



sol = Solution()
n = 12
primes = [2,7,13,19]
assert sol.nthSuperUglyNumber(n, primes) == 32

# n = 15
# primes =[3,5,7,11,19,23,29,41,43,47]
# print(sol.nthSuperUglyNumber(n, primes))