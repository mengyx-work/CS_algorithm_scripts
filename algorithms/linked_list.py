class Node(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node

    def get_val(self):
        return self.val

    def set_val(self, val):
        self.val = val

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

class LinkedList(object):
    '''
    Linked List
        referenced by https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/
        contains a head pointer to the head, may have another pointer to the tail

    methods:
        1. head_insert, insert a new Node as the new head
        2. search, search all the nodes by value
    '''
    def __init__(self, val=None):
        if val is not None:
            self.head = Node(val)
        else:
            self.head = None

    def __repr__(self):
        linked_list_content = "linked list: "
        cur = self.head
        while cur is not None:
            linked_list_content += " {},".format(cur.val)
            cur = cur.get_next_node()
        return linked_list_content 

    def head_insert(self, val):
        new_node = Node(val)
        new_node.set_next_node(self.head)
        self.head = new_node

    def search(self, val):
        '''
        search the linked list and try to find the node
        with node.val == val; if the node does not exist, a
        None pointer will return
        '''
        cur = self.head
        while cur is not None:
            if cur.val == val:
                break
            cur = cur.get_next_node()
        if cur is None:
            print "the linked list does not contain node with val {}...".format(val)
        return cur

    def delete(self, val):
        prev = None
        cur = self.head
        while cur is not None:
            if cur.val == val:
                break
            prev = cur
            cur = cur.get_next_node()
        if cur is None:
            print "the linked list does not contain node with val {}...".format(val)
        if prev is None:  # the node to delete is the head
            self.head = cur.get_next_node()
        else:
            prev.set_next_node(cur.get_next_node())


def main():
    linkedList = LinkedList()
    linkedList.head_insert(1)
    linkedList.head_insert(2)
    linkedList.head_insert(3)
    linkedList.head_insert(4)
    linkedList.delete(3)
    print linkedList


if __name__ == "__main__":
    main()
