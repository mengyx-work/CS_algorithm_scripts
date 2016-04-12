def smart_factorCombination(n, min_thres = 2):
    resList = []
    cur_num = n
    max_thres = int(n ** 0.5) + 1
    if min_thres > max_thres:
        return resList
    for i in range(min_thres, max_thres):
        if cur_num % i == 0:
            resList.append([i, cur_num/i])
            possible_combns = smart_factorCombination(cur_num/i, i)
            if len(possible_combns) != 0:
                for combn in possible_combns:
                    resList.append([i] + combn)

    return resList



smart_factorCombination(20)
