import sys

'''more specific on the boundaries: upperBound and lowerBound search
'''

def searchUpperBound(data, target):
    if data is None or len(data) == 0:
        return -1
    ## inialize the lb and up to -1 and len(data)
    lb, ub = -1, len(data)
    while (lb + 1 < ub):
        mid = lb + (ub - lb) / 2
        if data[mid] > target:
            ub = mid
        else:
            lb = mid
    return ub - 1

def searchLowerBound(data, target):
    if data is None or len(data) == 0:
        return -1
    lb, ub = -1, len(data)
    while lb + 1 < ub:
        mid = lb + (ub - lb) / 2
        if data[mid] < target:
            lb = mid
        else:
            ub = mid
    return lb + 1



def binarySearch(data, target, start_point):
	## contrain the final rearch to a list of small finite number of elements ##
	num_limit = 4
	if(len(data)<num_limit):
		for i in range(len(data)): ## loop through the interested list
			if(data[i]==target):
				index = start_point + i
				return index
			elif(i==(len(data)-1)): ## if not matching element is found
				return -1
			else:
				i += 1
	else:## use the stacked functions with proper return to create the binary search
		mid_index = int(len(data)/2)
		mid_value = data[mid_index]
		if(mid_value>target):
			return binarySearch(data[:mid_index], target, start_point)
		else:	
			return binarySearch(data[mid_index:], target, (mid_index+start_point))

	## tips on the final result: it's the index for the matching elment in the 
	## original list. So the proper start_point needs to be passed along the 
	## binary divisions. There are two indexes: local index to divide and the 
	## global one.
		



def main(argv):
	'''
	if(len(argv) != 3):
		print "Not enough arguments"
		sys.exit(0)
	else:
		honeycomb, max_layer_num = read_input(argv[1])
		read_dict(argv[2], honeycomb, max_layer_num)
	'''
	
	#input = open('input_data.txt', 'r')
	#data = [1, 3, 4, 6, 2 ,2, 8, 4, 8, 10]
	data = [1, 1, 4, 5, 6, 10, 12]
	## assumed the data list is sorted ##
	result = binarySearch(data, 14, 0)
	#print 'result: ', result
        data = [1, 2, 2, 4, 5]
        assert searchLowerBound(data, 2) == 1
        assert searchUpperBound(data, 2) == 2

        data = [1, 2, 2, 4, 5, 5, 5]
        assert searchLowerBound(data, 5) == 4
        assert searchUpperBound(data, 5) == 6


if __name__ == "__main__":
    main(sys.argv)
