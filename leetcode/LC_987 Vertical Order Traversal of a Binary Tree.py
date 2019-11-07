import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    # def verticalTraversal(self, root):
    #     indRes = collections.defaultdict(list)
    #     queue = [(root, 0)]
    #     while queue:
    #         next_queue = []
    #         queueRes = collections.defaultdict(list)
    #         for node, x in queue:
    #             if node is None:
    #                 continue
    #             queueRes[x].append(node.val)
    #             next_queue.append((node.left, x-1))
    #             next_queue.append((node.right, x+1))
    #         queue = next_queue
    #         for idx in queueRes:
    #             indRes[idx].extend(sorted(queueRes[idx]))
    #     return [indRes[idx] for idx in sorted(indRes)]


    def _verticalTraversal(self, root, x, y, indexRes):
        if root is None:
            return
        if x not in indexRes:
            indexRes[x] = {}
        if y not in indexRes[x]:
            indexRes[x][y] = []
        indexRes[x][y].append(root.val)
        self._verticalTraversal(root.right, x+1, y-1, indexRes)
        self._verticalTraversal(root.left, x-1, y-1, indexRes)


    def verticalTraversal(self, root):
        indexRes, res = {}, []
        self._verticalTraversal(root, 0, 0, indexRes)
        xkeys = list(indexRes.keys())
        xkeys.sort()
        for x in xkeys:
            yRes = []
            yKeys = list(indexRes[x])
            yKeys.sort(reverse=True)
            for y in yKeys:
                yRes.extend(sorted(indexRes[x][y]))
            res.append(yRes)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

sol = Solution()
print sol.verticalTraversal(root)