import sys


####################################################
## to search for the index for a certain element in
## a list, using quick sort and assuming the list is
## not sorted.
####################################################


#########################################################################

def SearchIndex(data, target):
	
	if(len(data)<4):
		for num, index in data:
			if(num==target):
 				return index

	else:      
		pivot_index = int(len(data)/2)
		#print 'pivot index: ', pivot_index
		pivot_value = data[pivot_index][0]

		less_pivot = []
		greater_pivot = []

		if(pivot_value==target):
			#print 'found the idnex: ', data[pivot_index][1] 
			return  data[pivot_index][1]
   
		for num, index in data:
	 		if(num<pivot_value):
 				less_pivot.append((num, index))        
			if(num>pivot_value):
				greater_pivot.append((num, index))        
    
		if(pivot_value>target):            
			return SearchIndex(less_pivot, target)
		if(pivot_value<target):            
 			return SearchIndex(greater_pivot, target)
        

#########################################################################

        
def searchInsert(nums, target):
	index = range(len(nums))
	data = zip(nums, index)
	print data
	print len(data)
	result = SearchIndex(data, target)
	if(result!=None):
		return result
	else:
		return 0

#########################################################################

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
	data = [1, 3, 4, 6, 23 ,2, 11, 32, 8, 10]
	#data = [1, 1 ,1, 1, 4, 5]
	result = searchInsert(data, 3)
	print result

if __name__ == "__main__":
    main(sys.argv)


