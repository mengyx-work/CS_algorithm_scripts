import sys

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
	print 'result: ', result

if __name__ == "__main__":
    main(sys.argv)
