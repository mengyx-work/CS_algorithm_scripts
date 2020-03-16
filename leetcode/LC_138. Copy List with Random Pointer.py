# """
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
# """

class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return None
        m = {head: Node(head.val)}
        queue = [head]
        while queue:
            cur = queue.pop()
            if cur.next is not None and cur.next not in m:
                queue.append(cur.next)
                m[cur.next] = Node(cur.next.val)
            if cur.next is not None:
                m[cur].next = m[cur.next]
            if cur.random is not None and cur.random not in m:
                queue.append(cur.random)
                m[cur.random] = Node(cur.random.val)
            if cur.random is not None:
                m[cur].random = m[cur.random]
        return m[head]



# class Solution(object):
#     m = {}
#     def copyRandomList(self, head):
#         if head is None:
#             return None
#         if head not in self.m:
#             self.m[head] = Node(head.val)
#             self.m[head].next = self.copyRandomList(head.next)
#             self.m[head].random = self.copyRandomList(head.random)
#         return self.m[head]