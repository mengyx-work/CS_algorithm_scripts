from collections import defaultdict
class Solution(object):
    def countArrangement(self, N):
        candidates = defaultdict(list)
        for i in xrange(1, N+1):
            for j in xrange(1, N+1):
                if (i % j == 0 and i >= j) or (j % i == 0 and j >= i):
                    candidates[i].append(j)

        meta_results = [[elem] for elem in candidates[1]]
        counts = 0
        while meta_results:
            result = meta_results.pop()
            if len(result) == N:
                counts += 1
                continue
            for elem in candidates[len(result)+1]:
                if elem not in result:
                    tmp_result = result[:]
                    tmp_result.append(elem)
                    meta_results.append(tmp_result)
        return counts
        '''
        for i in xrange(2, N+1):
            tmp_results = []
            for result in meta_results:
                #print 'candidates: ', i, candidates[i]
                for elem in candidates[i]:
                    if elem not in result:
                        tmp_result = result[:]
                        tmp_result.append(elem)
                        tmp_results.append(tmp_result)
            #print i, tmp_results
            meta_results = tmp_results[:]
        return len(meta_results)
        '''

sol = Solution()
#assert sol.countArrangement(1) == [[1]]
#assert sol.countArrangement(2) == [[1, 2,], [2,1]]
assert sol.countArrangement(2) == 2
assert sol.countArrangement(1) == 1
assert sol.countArrangement(4) == 8
                

     
