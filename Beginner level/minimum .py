def smallest_num_in_list( list ):
    min = list[ 0 ]
    for b in list:
        if b < min:
            min = b
    return min
print(smallest_num_in_list([2, 3, 1, 45,5]))
