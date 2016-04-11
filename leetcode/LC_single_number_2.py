import sys

def singleNumber(nums):
    product_1 = nums[0]
        
    i=1
    while(nums[i]^product_1!=0):
        print 'i:', i
        product_1 = product_1^nums[i]
        i += 1
    print 'the 2nd index: ', i        
    product_2 = nums[i]
        
    i += 1
    while(nums[i]^product_1!=0 or nums[i]^product_2!=0):
        if(nums[i]^product_1!=0):
            product_1 = product_1^nums[i]
        else:
            product_2 = product_2^nums[i]
        i += 1
                
    product_3 = nums[i]
        
    for k in range((i+1), len(nums)):
        if(nums[i]^product_1!=0):
            product_1 = product_1^nums[i]
        elif(nums[i]^product_2!=0):
            product_2 = product_2^nums[i]
        elif(nums[i]^product_3!=0):
            product_2 = product_3^nums[i]
        else:
            return nums[i]
        
    if(product_1==product_2):
        return (product_1^product_3) 
    if(product_1==product_3):
        return (product_1^product_2) 
    if(product_3==product_2):
        return (product_1^product_3) 

def main(argv):

    '''
    if(len(argv) != 3):
    	print "Not enough arguments"
    	sys.exit(0)
    else:
    	honeycomb, max_layer_num = read_input(argv[1])
    	read_dict(argv[2], honeycomb, max_layer_num)
    '''
    #data = [1, 2, 5, 9 ,12, 67]    
    data = [1, 2, 1, 1]    
    #data = [1]    
    print singleNumber(data)	

if __name__ == "__main__":
    main(sys.argv)





