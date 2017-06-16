class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def __repr__(self, level=0):
        print_output = '\t'*level + repr(self.val) + "\n"
        if self.left is not None:
            print_output += self.left.__repr__(level+1)
        if self.right is not None:
            print_output += self.right.__repr__(level+1)
        return print_output

    @staticmethod
    def _get_node_by_index(root, index):
        if index == 1:
            return root
        if index % 2 == 0:
            return TreeNode._get_node_by_index(root, index // 2).left
        else:
            return TreeNode._get_node_by_index(root, index // 2).right

    @classmethod
    def build_tree_from_array(cls, nums):
        if len(nums) == 0:
            return None
        root = cls(nums[0])
        for i, num in enumerate(nums[1:]):
            parent_index = (i + 2) // 2
            parent_node = cls._get_node_by_index(root, parent_index)
            if i % 2 == 0 and num is not None:
                parent_node.left = cls(num)
                continue
            if i % 2 == 1 and num is not None:
                parent_node.right = TreeNode(num)
        return root


from collections import deque
class Solution(object):
    @staticmethod
    def _push_child_nodes(hq, root_tuple):
        index, root = root_tuple[0], root_tuple[1]
        if root is None:
            return
        if root.left is not None:
            hq.append((index*2, root.left))
        if root.right is not None:
            hq.append((index*2+1, root.right))
            
    @classmethod
    def _remove_node(cls, heap):
        node = heap.popleft()
        cls._push_child_nodes(heap, node)

    def _insert_new_node_by_index(self, root_map, index, value):
        root = root_map[index // 2]
        if index % 2 == 0:
            root.left = TreeNode(value)
            root_map[index] = root.left
        else:
            root.right = TreeNode(value)
            root_map[index] = root.right

    def recursive_mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        root = TreeNode(t1.val + t2.val)
        if t1.left is not None or t2.left is not None:
            root.left = self.mergeTrees(t1.left, t2.left)
        if t1.right is not None or t2.right is not None:
            root.right = self.mergeTrees(t1.right, t2.right)
        return root

    def iterative_mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        t1_heap, t2_heap = deque([]), deque([])
        t1_value = 0 if t1 is None else t1.val
        t2_value = 0 if t2 is None else t2.val
        root = TreeNode(t1_value + t2_value)
        root_map = {1: root}

        self._push_child_nodes(t1_heap, (1, t1))
        self._push_child_nodes(t2_heap, (1, t2))
        
        while (t1_heap or t2_heap):
            t1_ptr, t2_ptr = None, None
            if t1_heap:
                t1_ptr = t1_heap[0]
            if t2_heap:
                t2_ptr = t2_heap[0]

            if t2_ptr is None:
                self._insert_new_node_by_index(root_map, t1_ptr[0], t1_ptr[1].val)
                self._remove_node(t1_heap)
                continue

            if t1_ptr is None:
                self._insert_new_node_by_index(root_map, t2_ptr[0], t2_ptr[1].val)
                self._remove_node(t2_heap)
                continue

            if t1_ptr[0] == t2_ptr[0]:
                self._insert_new_node_by_index(root_map, t1_ptr[0], (t1_ptr[1].val + t2_ptr[1].val))
                self._remove_node(t1_heap)
                self._remove_node(t2_heap)
            elif t1_ptr[0] < t2_ptr[0]:
                self._insert_new_node_by_index(root_map, t1_ptr[0], t1_ptr[1].val)
                self._remove_node(t1_heap)
            else:
                self._insert_new_node_by_index(root_map, t2_ptr[0], t2_ptr[1].val)
                self._remove_node(t2_heap)
        return root

nums1 = [1, 3, 2, 5]
nums2 = [2, 1, 3, None, 4, None, 7]
root1 = TreeNode.build_tree_from_array(nums1)
root2 = TreeNode.build_tree_from_array(nums2)
#print root1
#print root2
sol = Solution()
print sol.recursive_mergeTrees(root1, root2)
print sol.iterative_mergeTrees(root1, root2)
