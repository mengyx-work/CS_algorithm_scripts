import sys

def BitWise_XOR_List(data):
	result = 0
	for i in range(len(data)):
		result = result ^ data[i]
	return result
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
	#data = [1, 1 ,1, 1, 4, 5]
	data= [1 ,2, 4, 4, 2, 1, 6]
	result = BitWise_XOR_List(data)
	print result

if __name__ == "__main__":
    main(sys.argv)

