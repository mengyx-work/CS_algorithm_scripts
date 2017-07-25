class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        content = "{}".format(self.val)
        cur = self.next
        while cur is not None:
            content += "--> {}".format(cur.val)
            cur = cur.next
        return content
       
def build_linked_list(elem_list):
    if len(elem_list) == 0:
        return ListNode(None)
    head = ListNode(elem_list[0])
    cur = head
    for elem in elem_list[1:]:
        cur.next = ListNode(elem)
        cur = cur.next
    return head

def reverseList(head):
    cur, prev= head, None
    while cur is not None:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        '''
        use a dummy node to represent the
        head node
        '''
        dummy = ListNode(0)
        ptr = dummy
        ptr1, ptr2 = l1, l2
        while ptr1 is not None and ptr2 is not None:
            if ptr1.val < ptr2.val:
                ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                ptr.next = ptr2
                ptr2 = ptr2.next
            ptr = ptr.next
        ptr.next = ptr1 if ptr2 is None else ptr2
        return dummy.next


    '''
    def mergeTwoLists(self, l1, l2):
        ptr1, ptr2 = l1, l2
        head = None
        first = True
        while ptr1 is not None or ptr2 is not None:
            if ptr1 is None:
                if first:
                    ptr = ptr2
                else:
                    ptr.next = ptr2
                ptr2 = ptr2.next
            elif ptr2 is None:
                if first:
                    ptr = ptr1
                else:
                    ptr.next = ptr1
                ptr1 = ptr1.next
            else:
                if ptr1.val < ptr2.val:
                    if first:
                        ptr = ptr1
                    else:
                        ptr.next = ptr1
                    ptr1 = ptr1.next
                else:
                    if first:
                        ptr = ptr2
                    else:
                        ptr.next = ptr2
                    ptr2 = ptr2.next
            if first:
                head = ptr
                first = False
            else:
                ptr = ptr.next
        return head
        '''
        
head1 = build_linked_list([1, 3, 5])
head2 = build_linked_list([2, 4])
sol = Solution()
#print sol.mergeTwoLists(head1, head2)
head2 = build_linked_list([])
print sol.mergeTwoLists(head1, head2)

       
