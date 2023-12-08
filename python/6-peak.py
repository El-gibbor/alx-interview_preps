#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""

def find_peak(input_list):
    """recusively finds a peak in a given list"""
    if not input_list:
        return None

    if len(input_list) == 1:
        return input_list[0]
    elif len(input_list) == 2:
        return max(input_list)

    midl = len(input_list) // 2

    if input_list[midl] > input_list[midl - 1] and\
            input_list[midl] > input_list[midl + 1]:
                return input_list[midl]
    elif input_list[midl] < input_list[midl - 1]:
        return find_peak(input_list[:midl])
    elif input_list[midl] == input_list[midl - 1]: # case of equal sides
        left_peak = find_peak(input_list[:midl])
        right_peak = find_peak(input_list[midl:])
        return max(right_peak, left_peak)
    else:
        return find_peak(input_list[midl:])

# Complexity of this algorithm is O(log(n))
