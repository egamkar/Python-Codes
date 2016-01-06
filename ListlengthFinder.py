#! /usr/bin/env python
__author__ = 'egamkar'

def ListLengthFinder():
    input = raw_input("please input the list")

    input_list = input.split()

    count = 0

    for char in input_list:
        count += 1

    print count

ListLengthFinder()
