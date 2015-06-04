import sys

def merge(A, B):
	merged_list = []
	i, j=0, 0
	A_len, B_len = len(A), len(B)

	while i<A_len and j<B_len:
		if(A[i]<B[j]):
			merged_list.append(A[i])
			i += 1
		else:
			merged_list.append(B[j])
			j += 1

	merged_list += A[i:]
	merged_list += B[j:]


	'''
	for _ in range(0, (A_len+B_len)):
		if (i<A_len) and ((A[i]<B[j] or j>=B_len)):
			merged_list.append(A[i])
			i += 1
		else:
			merged_list.append(B[j])
			j += 1
	'''
	return merged_list


def mergeSort(data):
	
	if(len(data)<2):
		return data

	mid_index = int(len(data)/2)
	A = mergeSort(data[0:mid_index])
	B = mergeSort(data[mid_index:])

	return merge(A, B)

		




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
	data = [1, 3, 4, 6, 2 ,2, 8, 4, 8, 10]
	#data = [1, 1 ,1, 1, 4, 5]
	result = mergeSort(data)
	print result

if __name__ == "__main__":
    main(sys.argv)
