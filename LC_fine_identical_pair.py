import sys

############################################
## algorithm is similar to the quick sort,
## tries to divide the data by a pivot point
## each time and continue recursively
############################################
def containsDuplicate(nums):
	## when the elemen# is small enough, do it manually
	if(len(nums)<4):
		for elem in nums:
			nums.remove(elem)
			if(elem in nums):
				return True
		return False

	## divide the datase by pivot value
	pivot_index = int(len(nums)/2)
	pivot_value = nums[pivot_index]
	
	nums.remove(pivot_value)    ##to avoid the duplicated count
	less_pivot = []
	greater_pivot = []

	for elem in nums:
		if(elem==pivot_value):
			return True
		if(elem<pivot_value):
			less_pivot.append(elem)
		if(elem>pivot_value):
			greater_pivot.append(elem)

	return (containsDuplicate(less_pivot) or containsDuplicate(greater_pivot))
################################################

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
	data=[1, 2, 3, 4]
	#data = [1, 1 ,1, 1, 4, 5]
	result = containsDuplicate(data)
	print result

if __name__ == "__main__":
    main(sys.argv)


