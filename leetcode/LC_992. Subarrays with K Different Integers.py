# class Solution(object):
#     def subarraysWithKDistinct(self, A, K):
#         count, stack = 0, []
#         for i in range(0, len(A)-K+1):
#             stack.append((i, i, {A[i]}))
#         while stack:
#             st, ed, cur = stack.pop()
#             if len(cur) > K:
#                 continue
#             if len(cur) == K:
#                 count += 1
#             if ed == (len(A) - 1):
#                 continue
#             ed += 1
#             cur.add(A[ed])
#             stack.append((st, ed, cur))
#         return count

'''
int subarraysWithKDistinct(vector<int>& A, int K, int res = 0) {
  vector<int> m(A.size() + 1);
  for(auto i = 0, j = 0, prefix = 0, cnt = 0; i < A.size(); ++i) {
    if (m[A[i]]++ == 0) ++cnt;
    if (cnt > K) --m[A[j++]], --cnt, prefix = 0;
    while (m[A[j]] > 1) ++prefix, --m[A[j++]];
    if (cnt == K) res += prefix + 1;
  }
  return res;
}
'''

from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        prefix, res, count = 0, 0, 0
        l, r = 0, 0
        counts = defaultdict(int)
        while r < len(A):
            if counts[A[r]] == 0:
                count += 1
            counts[A[r]] += 1

            if count > K:
                prefix = 0
                counts[A[l]] = 0
                count -= 1
                l += 1

            ## move the left index to num that only shows up once
            while counts[A[l]] > 1:
                counts[A[l]] -= 1
                l += 1
                prefix += 1

            if count == K:
                res += prefix + 1
            # print('#2 ', l, r, res, counts)

            r += 1
        return res


class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        prefix, res, count = 0, 0, 0
        l, r = 0, 0
        counts = defaultdict(int)
        while r < len(A):
            if counts[A[r]] == 0:
                count += 1
            counts[A[r]] += 1

            if count > K:
                prefix = 0
                while count > K:
                    counts[A[l]] -= 1
                    if counts[A[l]] == 0:
                        count -= 1
                    l += 1

            ## move the left index to num that only shows up once
            while counts[A[l]] > 1:
                counts[A[l]] -= 1
                l += 1
                prefix += 1

            if count == K:
                res += prefix + 1
            # print('#2 ', l, r, res, counts)

            r += 1
        return res


sol = Solution()
A = [1,2,1,2,3]
K = 3
print(sol.subarraysWithKDistinct(A, K))