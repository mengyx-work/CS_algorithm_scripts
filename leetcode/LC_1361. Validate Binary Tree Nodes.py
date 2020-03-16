# class Solution(object):
#     def validateBinaryTreeNodes(self, n, leftChild, rightChild):
#         root = None
#         for i in range(n):
#             if i not in leftChild and i not in rightChild:
#                 if root is None:
#                     root = i
#                 else:
#                     return False
#         visited = [0 for _ in range(n)]
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             # print(node, visited)
#             if visited[node] == 1:
#                 return False
#             visited[node] = 1
#             if leftChild[node] != -1:
#                 stack.append(leftChild[node])
#             if rightChild[node] != -1:
#                 stack.append(rightChild[node])
#         return True


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        root = None
        for i in range(n):
            if i not in leftChild and i not in rightChild:
                if root is None:
                    root = i
                else:
                    return False
        if root is None:
            return False
        visited = [0 for _ in range(n)]
        stack = [root]
        while stack:
            next_stack = []
            for node in stack:
                if visited[node] == 1:
                    return False
                visited[node] = 1
                if leftChild[node] != -1:
                    next_stack.append(leftChild[node])
                if rightChild[node] != -1:
                    next_stack.append(rightChild[node])
            stack = next_stack[:]
        return True

sol = Solution()
# leftChild = [1,-1,3,-1]
# rightChild = [2,3,-1,-1]
# assert sol.validateBinaryTreeNodes(4, leftChild, rightChild) == False


leftChild = [1,0]
rightChild = [-1,-1]
assert sol.validateBinaryTreeNodes(2, leftChild, rightChild) == False