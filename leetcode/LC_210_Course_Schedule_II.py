class Solution(object):

    def _dsf(self, currentCourse, sequence, dependentOnDict, states):
        # print currentCourse, sequence, originalCourse
        if currentCourse in sequence:
            return 0

        if states[currentCourse] == 1:
            return -1

        states[currentCourse] = 1
        if currentCourse not in dependentOnDict:
            sequence.append(currentCourse)
        else:
            for dependentCourse in dependentOnDict[currentCourse]:
                sign = self._dsf(dependentCourse, sequence, dependentOnDict, states)
                if sign == -1:
                    return -1
            sequence.append(currentCourse)
        return 0

    def findOrder(self, numCourses, prerequisites):
        dependentOnDict, states = {}, {}

        for prerequisite in prerequisites:
            dependentCourse, startCourse = prerequisite
            if dependentCourse not in dependentOnDict:
                dependentOnDict[dependentCourse] = []
            dependentOnDict[dependentCourse].append(startCourse)

        for i in range(numCourses):
            states[i] = 0

        sequence = []
        for course in range(numCourses):
            sign = self._dsf(course, sequence, dependentOnDict, states)
            if sign == -1:
                return []
        return sequence


sol = Solution()
# print sol.findOrder(2, [[1,0]])
assert sol.findOrder(2, [[1,0]]) ==[0, 1]
assert sol.findOrder(4, [[1,0], [2,0], [3,1], [3,2]]) == [0, 1, 2, 3]
assert sol.findOrder(3, [[1,1]]) == []
assert sol.findOrder(4, [[0,1], [3,1], [1,3], [3,2]]) == []






