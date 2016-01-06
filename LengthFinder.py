#! /usr/bin/env python
__author__ = 'egamkar'

def LengthFinder():
    input_0 = raw_input("please input the type: either List or String")
    input_1 = raw_input("please input for finding the length")

    if input_0 == "String":
        input_list = input_1
    elif input_0 == "List":
        input_list = input_1.split()
    else:
        print "wrong 1st argument entered"
        exit()

    count = 0

    for char in input_list:
        count += 1

    print count

LengthFinder()