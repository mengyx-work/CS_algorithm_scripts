import sys

def sheet_column_number(column_string):
	column = list(column_string.lower()) ## list a string to convert it into a list of characters
	column_number = 0
	order = range(len(column))

	for char, i in zip(reversed(column), order):
		print char, i
		column_number += (ord(char)-96)*(26**i)
		print column_number
	return column_number

	'''
	for char in reversed(column_count):
		column_number += (ord(char)-96) + (column*24)
		column += 1
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
	
	print sheet_column_number('AAB')	

if __name__ == "__main__":
    main(sys.argv)



