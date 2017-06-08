class Node(object):
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self):
        return 'value: {}, left: ({}), right: ({})'.format(self.val, "" if self.left is None else self.left, "" if self.right is None else self.right)

def print_inOder(root):
    if root:
        print_inOder(root.left)
        print root.val
        print_inOder(root.right)

def _create_tree(nums):
    root = None
    for i, num in enumerate(nums):
        cur_i = i + 1
        parent_index = [cur_i]
        while cur_i // 2 > 0:
            cur_i = cur_i // 2
            parent_index.append(cur_i)

        parent_index = parent_index[:-1]
        if len(parent_index) == 0:
            root = Node(num)
            continue
        cur_node = root
        ## use the parent index to trace to the current node
        parent_index = parent_index[::-1]
        print i, parent_index
        for index in parent_index[:-1]:
            if index % 2 == 0:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        if  parent_index[-1] % 2 == 0:
            cur_node.left = Node(num)
        else:
            cur_node.right = Node(num)
    return root

nums = range(1, 8)
root = _create_tree(nums)
print root
#root = Node(1)
#cur_node = Node(2)
#print root
