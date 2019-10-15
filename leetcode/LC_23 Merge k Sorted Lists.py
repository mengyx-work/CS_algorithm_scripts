import heapq

## Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        curHead = dummyHead
        h = []
        for i in range(len(lists)):
            if lists[i] is not None:
                heapq.heappush(h, (lists[i].val, i))
        while len(h) > 0:
            val, index = heapq.heappop(h)
            curHead.next = ListNode(val)
            curHead = curHead.next
            if lists[index].next is not None:
                lists[index] = lists[index].next
                heapq.heappush(h, (lists[index].val, index))
        return dummyHead.next

