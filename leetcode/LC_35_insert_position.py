import sys


def Return_SearchIndex(data, target, offset):
    print 'offset: ', offset
    if len(data)<3:
        if data[0]>=target:
            return (0 + offset)
        elif len(data)==1:
            return (1 + offset)
        if target>data[1]:
            return (2 + offset)
        else:
            return (1 + offset)

    else:
        mid_index = (len(data))/2
        mid_value = data[mid_index]
        print 'mid_value: ', mid_value
        if mid_value==target:
            return (mid_index + offset)
        if mid_value>target:
            return Return_SearchIndex(data[:mid_index], target, offset)
        else:
            return Return_SearchIndex(data[mid_index:], target, (mid_index+offset))



def SearchIndex(data, target):
    if len(data)<3:
        return Return_SearchIndex(data, target, 0)
    else:
        mid_index = (len(data)-1)/2 ## to properly define the mid_index for an array, but biased split should not matter
        mid_value = data[mid_index]

        if mid_value==target:
            return mid_index
        if mid_value>target:
            return Return_SearchIndex(data[:mid_index], target, 0)
        else:
            return Return_SearchIndex(data[mid_index:], target, mid_index)


def main(argv):

    '''
    if(len(argv) != 3):
    	print "Not enough arguments"
    	sys.exit(0)
    else:
    	honeycomb, max_layer_num = read_input(argv[1])
    	read_dict(argv[2], honeycomb, max_layer_num)
    '''
    data = [1, 2, 5, 9 ,12, 67]    
    #data = [1]    
    print SearchIndex(data, 5)	

if __name__ == "__main__":
    main(sys.argv)




