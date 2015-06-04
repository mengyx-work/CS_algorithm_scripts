# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_pair_num(case_data, case_length):
    pair_count = 0
    for i in range(case_length-1):
        #print 'the i: ', i
        #print 'pair_count: ', pair_count
        test_element = case_data[i]
        #print 'original data: ', case_data
        case_data.remove(test_element)
        #print 'new set: ', case_data
        if(test_element in case_data):
            case_data.remove(test_element)
            pair_count += 2
        if (len(case_data)==1):
            break
        
    return pair_count
    
case_num = raw_input()
for i in range(int(case_num)):
    case_length = raw_input()
    case_data = raw_input().split()
    case_data  = [int(x) for x in case_data]
    pair_num = get_pair_num(case_data, int(case_length))
    print pair_num
