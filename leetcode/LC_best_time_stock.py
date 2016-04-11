import sys

def maxProfit(data):
	if(len(data)<2):
		return 0
	diff_data = [int(data[i+1]-data[i]) for i in range(len(data)-1)]
	#return diff_data
	profit = 0
	for i in range(len(diff_data)):
		if(diff_data[i]>0):
			profit += diff_data[i]
	return profit

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
	data = [1, 3, 4, 6, 2 ,2, 8, 4, 8, 10]
	#data = [1, 1 ,1, 1, 4, 5]
	result = maxProfit(data)
	print result

if __name__ == "__main__":
    main(sys.argv)

