class min_heap(object):
    def __init__(self, current_size, heap=None):
        self.current_size = current_size
        if heap is None:
            self.heap = []
        else:
            self.heap = heap

    def heapify(self):
        for i in range(self.current_size-1, 0):
            self._float_up(i)

    def insert(self, elem):
        self.heap.append(elem)
        self.current_size += 1
        self._float_up(current_size-1)

    def _get_child_index(self, i):
        if i > self.current_size // 2:
            raise ValueError('index {} is not a valid parent node...'.format(i))
        return 2*i+1, 2*2+2

    def _get_parent_index(self, i):
        if i == 0:
            print 'already reached root...'
            return 0
        if i % 2 == 0:
            return i / 2 - 1
        else:
            return i // 2

    def _swap_element(self, i, j):
        self.heap[i], self.heap[j] =  self.heap[j], self.heap[i]  

    def _sink_down(self, i):
        ''' from any index, to sink
        the element down to the proper location,
        which fits the min_heap
        it 
        '''
        if i < self.current_size // 2:
            left_child, right_child = self._get_child_index(i)
        max_value_index = i
        if left_child < self.current_size and self.heap[left_child] > self.heap[max_value_index]:
            max_value_index = left_child
        if right_child < self.current_size and self.heap[right_child] > self.heap[max_value_index]:
            max_value_index = right_child
        if max_value_index != i:
            self._swap_element(max_value_index, i)
            self._sink_down(max_value_index)

    def _float_up(self, i):
        ''' different approaches:
        recursive function call
        or iterative in while loop
        '''
        if i ==  0:
            return 
        parent_index = self._get_parent_index(i)
        if sel.heap[parent_index] > self.heap[i]:
            self._swap_element(i, parent_index)
            self._float_up(parent_index)

        '''
        while (i > 0):
            parent_index = self._get_parent_index(i)
            if sel.heap[parent_index] > self.heap[i]:
                self._swap_element(i, parent_index)
                i = parent_index
            else:
                break
        '''

def main():
    nums = [4, 5, 7, 3]
    minHeap = min_heap(
