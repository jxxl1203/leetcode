def merge_m_array(list):
    index = [0 for i in range(len(list))]
    res = []
    while 1:
        min_num = float('inf')
        index_set = set()
        for i in range(len(list)):
            if index[i] >= len(list[i]):
                continue
            if list[i][index[i]] < min_num:
                index_set = set()
                min_num = list[i][index[i]]
                index_set.add(i)
            elif list[i][index[i]] == min_num:
                index_set.add(i)
        i = 0
        if len(index_set) == 0:
            break
        for i in index_set:
            index[i] += 1
        res.append(list[i][index[i]-1])
    return res


print merge_m_array([[1,2,4,7],[2,3,5,9],[4,6,8,10]])