# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_pair_num(case_data, case_length):
    pair_count = long(0)
    for i in range(case_length-1):
        #print 'the i: ', i
        #print 'pair_count: ', pair_count
        test_element = case_data[0]
        #print 'data set: ', case_data
        case_data.remove(test_element)
        for element in case_data:
            if(element==test_element):
                pair_count += 2
        #print 'new set: ', case_data
        #if(test_element in case_data):
            #case_data.remove(test_element)
            #pair_count += 2
            
    return pair_count

#case_data = [1, 1, 2, 1, 1]
#case_length = len(case_data)
#pair_num = get_pair_num(case_data, int(case_length))
#print pair_num
   
case_num = raw_input()
for i in range(int(case_num)):
    case_length = raw_input()
    case_data = raw_input().split()
    case_data  = [int(x) for x in case_data]
    pair_num = long(0)
    pair_num = get_pair_num(case_data, int(case_length))
    print pair_num

