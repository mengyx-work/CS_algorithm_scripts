class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []
        for elem in asteroids:
            if not stack:
                stack.append(elem)
            else:
                if stack[-1] > 0 and elem < 0:
                    while stack and stack[-1] > 0 and elem < 0:
                        otherElem = stack.pop()
                        if abs(otherElem) == abs(elem):
                            elem = None
                            break
                        elif abs(otherElem) > abs(elem):
                            elem = otherElem
                    if elem is not None:
                        stack.append(elem)
                else:
                    stack.append(elem)
        return stack

sol = Solution()
asteroids = [10, 2, -5]
assert sol.asteroidCollision(asteroids) == [10]
asteroids = [-2, -1, 1, 2]
assert sol.asteroidCollision(asteroids) == [-2, -1, 1, 2]
asteroids = [8, -8]
assert sol.asteroidCollision(asteroids) == []


