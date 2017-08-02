from collections import defaultdict
from Queue import Queue
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        preReqDict = defaultdict(set)
        neighborDict = defaultdict(list)
        for course, preReq in prerequisites:
            preReqDict[course].add(preReq)
            neighborDict[preReq].append(course)
        res = []
        # the BFS approach, the next-level adjacent nodes is pushed back to the end of queue
        seeds = Queue()
        # the DFS approaach, the next-level adjacent node is popped out
        stack_seeds = []
        for i in xrange(numCourses):
            if i not in preReqDict.keys():
                seeds.put(i)
                stack_seeds.append(i)
        #while not seeds.empty():
        while len(stack_seeds) > 0:
            #course = seeds.get()
            course = stack_seeds.pop()
            res.append(course)
            for adj_course in neighborDict[course]:
                preReqDict[adj_course].remove(course)
                if len(preReqDict[adj_course]) == 0:
                    seeds.put(adj_course)
                    stack_seeds.append(adj_course)
                    preReqDict.pop(adj_course)
        if len(res) == numCourses:
            return True
        else:
            return False

sol = Solution()
assert sol.canFinish(2, [[1,0]]) == True
assert sol.canFinish(2, [[1,0], [0, 1]]) == False





