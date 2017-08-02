class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        courseSeq = []
        prereqCourse = {}
        for pair in prerequisites:
            if pair[0] not in prereqCourse:
                prereqCourse[pair[0]] = {}
            prereqCourse[pair[0]].add(pair[1])
        for i in xrange(numCourses):
            if i not in prereqCourse.keys():
                courseSeq.append(i)
        prev_course_count = 0
        while len(courseSeq) > prev_course_count:
            prev_course_count = len(courseSeq)
            for key in prereqCourse.keys():
                if reduce(lambda x, y: x and y, [elem in courseSeq for elem in prereqCourse[key]]):
                    courseSeq.append(key)
                    prereqCourse.pop(key)
        if len(prereqCourse) == 0:
            return courseSeq
        else:
            return []

sol = Solution()
assert sol.findOrder(2, [[1,0]]) ==[0, 1]
assert sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0, 1, 2, 3]
assert sol.findOrder(3, [[1,1]]) == []






