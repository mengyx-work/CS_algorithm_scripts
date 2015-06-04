import sys

def partition(data_list, low_index, high_index):
	pivot_index = (low_index+int((high_index-low_index)/2))
	#pivot_index = low_index+1
	pivot_value = data_list[pivot_index]
	## swap the pivot and last elments
	data_list[high_index], data_list[pivot_index] = data_list[pivot_index], data_list[high_index]

	StoreIndex = low_index
	for i in range(low_index, high_index):
		identi_count = 0
		if(data_list[i]<=pivot_value):
			if(data_list[i]==pivot_value):
				identi_count += 1 ## only move once to reduce the index of repeated elements
			print 'data_list[i], pivot_value: ',data_list[i],  pivot_value
			data_list[StoreIndex], data_list[i] = data_list[i], data_list[StoreIndex]
			StoreIndex += 1
			print 'identi_count, StoreIndex: ', identi_count, StoreIndex

	## swap the pivot and last elments
	data_list[high_index], data_list[StoreIndex] = data_list[StoreIndex], data_list[high_index]

	return (StoreIndex-identi_count)


def quickSort(data_list, low_index, high_index):
	if(low_index<high_index):
		print 'low_index, high_index: ', low_index, high_index
		#print 'data: ', data_list
		partition_point = partition(data_list, low_index, high_index)
		print 'partition_point: ', partition_point
		if((high_index-low_index)!=1):
			quickSort(data_list, partition_point, high_index)
			quickSort(data_list, low_index, partition_point)



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
	data = [1, 1 ,1, 1, 4, 5]
	quickSort(data, 0, len(data)-1)
	print data

if __name__ == "__main__":
    main(sys.argv)
