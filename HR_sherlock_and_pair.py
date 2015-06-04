## learn from the quickSort, to collect the repeated elements
def found_multi(data, element_count):
    less = []
    greater = []
    equal_count = 0
    if(len(data)>1):
        pivot_index = int(len(data)/2)
        pivot_value = data[pivot_index]

        for element in data:
            if(element<pivot_value):
                less.append(element)
            if(element>pivot_value):
                greater.append(element)            
            if(element==pivot_value):
                equal_count +=1
        if(equal_count>1):
            element_count[pivot_value] = equal_count
        found_multi(less, element_count)
        found_multi(greater, element_count)
                
        
        
## create a dict to hold all the repaeated elements and counts
## the pair_count value is k*(k-1)        
def get_pair_num(case_data, case_length):
    pair_count = long(0)
    element_count = {}
    found_multi(case_data, element_count)
    #print 'dict: ', element_count
    for key in element_count:
        value = long(element_count[key])
        #print 'single value: ', value
        pair_count += value*(value-1)
        
    return pair_count

#case_data = [1, 1, 2, 1, 1, 2, 2, 4, 4]
#case_length = len(case_data)
#pair_num = get_pair_num(case_data, int(case_length))
#print 'result', pair_num
   
case_num = raw_input()
for i in range(int(case_num)):
    case_length = raw_input()
    case_data = raw_input().split()
    case_data  = [int(x) for x in case_data]
    pair_num = long(0)
    pair_num = get_pair_num(case_data, int(case_length))
    print pair_num

