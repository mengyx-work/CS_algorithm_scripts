class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        ptr_1, ptr_2 = head, head
        while ptr_1.next is not None and ptr_2.next is not None and ptr_2.next.next is not None:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next.next
            if ptr_1 == ptr_2:
                return True
        return False
            


