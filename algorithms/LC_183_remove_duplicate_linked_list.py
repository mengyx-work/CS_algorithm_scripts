# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        content = "{} --> ".format(self.val)
        cur = self.next
        while cur is not None:
            content += "{} --> ".format(cur.val)
            if cur.next is None:
                break
            cur = cur.next
        content += "None"
        return content

class LinkedList(object):
    def __init__(self, x=None):
        if x is not None:
            self.head = ListNode(x)
        else:
            self.head = None

    def __repr__(self):
        content = ""
        cur = self.head
        while cur is not None:
            content += "{} --> ".format(cur.val)
            cur = cur.next
        content += "None"
        return content

    def add_tail(self, x):
        if self.head is None:
            self.head = ListNode(x)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = ListNode(x)

class Solution(object):
    def deleteDuplicates(self, head):
        cur = head
        while cur:
            if cur.next is not None and cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
                

sol = Solution()
linked_list = LinkedList(1) 
linked_list.add_tail(1)
linked_list.add_tail(1)
print linked_list.head
sol.deleteDuplicates(linked_list.head)
print linked_list.head

linked_list = LinkedList(1)
print linked_list.head
sol.deleteDuplicates(linked_list.head)
print linked_list.head

