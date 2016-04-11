import sys

def quickSort(data):

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
	result = quickSort(data)
	print result

if __name__ == "__main__":
    main(sys.argv)
