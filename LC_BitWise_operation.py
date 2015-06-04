import sys

def bitLenCount(int_type):
	length = 0
	count = 0
	while (int_type):
		count += (int_type & 1)
		length += 1
		int_type >>= 1
	return(length, count)


def main(argv):
	'''
	if(len(argv) != 3):
		print "Not enough arguments"
		sys.exit(0)
	else:
		honeycomb, max_layer_num = read_input(argv[1])
		read_dict(argv[2], honeycomb, max_layer_num)
	'''
	
	print bitLenCount(7)	

if __name__ == "__main__":
    main(sys.argv)


