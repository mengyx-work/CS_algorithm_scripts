'''
heap sort uses the special tree-based data structure heap to 
sort the array in a different pattern inplace. 
for a heap based on binary tree:
1. two child nodes are smaller than the parent node
2. for each element n in the array: the left/right 
child nodes are 2 * n + 1 and 2 * n + 2
'''
def swap_elements(i, j, aList):
    aList[i], aList[j] = aList[j], aList[i]

def heapify(start, end, aList):
    '''
    function to heapify the element at 
    start index as tree node based, with
    end index limit
    there is a recursive call to heapify
    to make sure that swap does not change
    the heap
    '''
    left_child_index = 2 * start + 1
    right_child_index = 2 * start + 2 
    max_value_index = start

    if left_child_index < end and aList[max_value_index] < aList[left_child_index]:
        max_value_index = left_child_index

    if right_child_index < end and aList[max_value_index] < aList[right_child_index]:
        max_value_index = right_child_index

    if max_value_index != start:
        swap_elements(start, max_value_index, aList)
        heapify(max_value_index, end, aList)

def heap_sort(aList):
    end = len(aList)
    max_parent_index = end // 2 - 1
    for i in range(max_parent_index, -1, -1):
        heapify(i, end, aList)
        
    for i in range(end - 1, 0, -1):
        swap_elements(0, i, aList)
        heapify(0, i, aList)


sqc = [2, 7, 1, -2, 56, 5, 3]
heap_sort(sqc)
print(sqc)


