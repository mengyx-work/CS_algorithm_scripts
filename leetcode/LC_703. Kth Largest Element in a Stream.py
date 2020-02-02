import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > self.k:
            heapq.heappop(self.pool)

    def add(self, val):
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

    # def __init__(self, k, nums):
    #     nums.sort(reverse=True)
    #     self.arr = nums
    #     sorted(self.arr, reverse=True)
    #     self.k = k
    #     self.arr = self.arr[:self.k]
    #
    # def add(self, val):
    #     self.arr.append(val)
    #     for i in range(len(self.arr)-1, 0, -1):
    #         j = i - 1
    #         if self.arr[j] < self.arr[i]:
    #             self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    #     self.arr = self.arr[:self.k]
    #     return self.arr[-1]


k = 3
nums = [4,5,8,2]
obj = KthLargest(k, nums)
param_1 = obj.add(3)
print(param_1)
param_1 = obj.add(5)
# param_1 = obj.add(10)
print(param_1)