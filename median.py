__author__ = 'changhan.ryu'

// find the median value of the list

def median(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) % 2 == 1:
        return sorted_lst[len(sorted_lst) // 2]

    return (sorted_lst[(len(sorted_lst) // 2) -1] + sorted_lst[len(sorted_lst) // 2]) / 2.0
