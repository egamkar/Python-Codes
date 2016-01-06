#! /usr/bin/env python

__author__ = 'egamkar'

input_string = raw_input("please input rguments with space in between")


input_list = input_string.split();

count = 0

max_number = 0

for numbers in input_list:
    if int(numbers) > max_number:
        max_number = int(numbers)


print max_number
