#!/usr/bin/python3
"""a function that converts a roman numeral to an integer"""

def roman_to_int(roman_str):
    if not isinstance(roman_str, str) or roman_str is None:
        return 0

    # map all roman numerals to their corresponding value
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    to_int, prev_value = 0, 0

    for roman in reversed(roman_str):
        value = roman_nums[roman]
        if value >= prev_value:
            to_int += value
        else:
            to_int -= value
        prev_value = value  # holds L11 at each iteration after validating L12

    return to_int
