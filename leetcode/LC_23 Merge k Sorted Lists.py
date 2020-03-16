import heapq

## Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        cur = dummy
        hq = []
        for e in lists:
            if e is not None:
                heapq.heappush(hq, (e.val, e))
        while hq:
            _, l = heapq.heappop(hq)
            cur.next = l
            if l.next is not None:
                next_l = l.next
                heapq.heappush(hq, (next_l.val, next_l))
            cur = cur.next
            cur.next = None
        return dummy.next


# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         dummyHead = ListNode(0)
#         curHead = dummyHead
#         h = []
#         for i in range(len(lists)):
#             if lists[i] is not None:
#                 heapq.heappush(h, (lists[i].val, i))
#         while len(h) > 0:
#             val, index = heapq.heappop(h)
#             curHead.next = ListNode(val)
#             curHead = curHead.next
#             if lists[index].next is not None:
#                 lists[index] = lists[index].next
#                 heapq.heappush(h, (lists[index].val, index))
#         return dummyHead.next

