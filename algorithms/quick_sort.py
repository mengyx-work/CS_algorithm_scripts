import sys, random

def  partition(data, start, end):
    pivot = start
    #print 'using pivot: ', pivot
    ## the data[start] is used as refernce value
    for i in range(start+1, end+1):
        if data[i] <= data[start]:
            pivot += 1
            data[pivot], data[i] = data[i], data[pivot]
    data[pivot], data[start] = data[start], data[pivot]
    return pivot


def _quickSort(data, start, end):
    if start >= end:
        return
    pivot = partition(data, start, end)
    _quickSort(data, pivot+1, end)
    _quickSort(data, start, pivot-1)

def quickSort(data):
    start, end = 0, len(data) - 1
    if start >= end:
        return
    _quickSort(data, start, end)

'''
def quickSort(data):
    ## demo for the idea of quickSort
    ## Not implemented as inplace sort
    less_pivot = []
    equal_pivot = []
    greater_pivot = []
    if(len(data)>1):
        pivot_index = int(len(data)/2)
	pivot_value = data[pivot_index]
	for element in data:
	    if(element<pivot_value):
	        less_pivot.append(element)
	    if(element==pivot_value):
		equal_pivot.append(element)
            if(element>pivot_value):
	        greater_pivot.append(element)
	return 	quickSort(less_pivot) + equal_pivot + quickSort(greater_pivot)
    else:
	return data
'''
		




def main(argv):
	'''
	if(len(argv) != 3):
		print "Not enough arguments"
		sys.exit(0)
	else:
		honeycomb, max_layer_num = read_input(argv[1])
		read_dict(argv[2], honeycomb, max_layer_num)
	'''
	
        result = [i for i in range(100)]
        for i in range(50):
            data = result[:]
            random.shuffle(data)
            quickSort(data)
            assert data == result

	result = [1, 1 ,1, 1, 4, 5]
        data = result[:]
	quickSort(data)
        assert result == data

if __name__ == "__main__":
    main(sys.argv)
