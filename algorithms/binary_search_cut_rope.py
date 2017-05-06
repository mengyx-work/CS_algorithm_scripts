import sys

def round_off(num):
    return float('{:.2f}'.format(num))

def can_cut_rope(lenghts, k, pieceLen):
    count = 0
    for length in lenghts:
        count += int(length / pieceLen)
    if count >= k:
        return True
    return False


def cut_ropes(n, lenghts, k):
    min_len, max_len = 0., round_off(sum(lenghts) / k)
    ## critical to consider the step
    ## 0.01 or the index 1 in the while
    while(min_len + 0.01 < max_len):
        mid_len = round_off(min_len + (max_len - min_len) / 2)
        if can_cut_rope(lenghts, k, mid_len):
            min_len = mid_len
        else:
            max_len = mid_len
        print mid_len, min_len, max_len
    return min_len


    

def main(argv):
    N = 4
    K = 11
    L = [8.02, 7.43, 4.57, 5.39]
    print round_off(0.239)
    print cut_ropes(N, L, K)

if __name__ == '__main__':
    main(sys.argv)


