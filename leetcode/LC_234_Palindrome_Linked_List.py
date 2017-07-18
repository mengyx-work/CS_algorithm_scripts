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

def count_length(head):
    length = 0
    cur = head
    while cur is not None:
        length += 1
        cur = cur.next
    return length

def reach_node_by_step(head, steps):
    if steps == 0:
        return head
    cur = head
    for _ in xrange(steps):
        cur = cur.next
    return cur

class Solution(object):
    def isPalindrome(self, head):
        length = count_length(head)
        if length <= 1:
            return True
        steps = length // 2 - 1
        head_1_tail = reach_node_by_step(head, steps)
        head_2 = head_1_tail.next
        head_1_tail.next = None
        head_2 = reverseList(head_2)
        cur_1 = head
        cur_2 =head_2 
        print cur_1
        print cur_2
        while cur_2 is not None and cur_1 is not None:
            if cur_2.val != cur_1.val:
                return False
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        return True

sol = Solution()
'''
content = range(5)
head = build_linked_list(content + content[::-1])
#print head
assert sol.isPalindrome(head) == True
head = build_linked_list(content + [2, 3] +  content[::-1])
assert sol.isPalindrome(head) == False
'''
head = build_linked_list([1, 0, 1])
print sol.isPalindrome(head)

       
