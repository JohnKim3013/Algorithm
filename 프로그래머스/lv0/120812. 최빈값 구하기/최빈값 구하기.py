def solution(array):
    a = sorted(list(set(array)))
    my_dict = {}
    for i in a:
        my_dict[i] = array.count(i)
    # print(my_dict)    
    max_list = [k for k,v in my_dict.items() if max(my_dict.values()) == v]
    # print(max_list)
    if len(max_list) == 1:
        return max_list[0]
    else:
        return -1

        
    