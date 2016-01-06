#! /usr/bin/env python
__author__ = 'egamkar'

def MaxFinder():
    input_string = raw_input("please input arguments with : in between")


    input_list = input_string.split(':');

    print input_string

    print input_list

    max_number = 0

    for numbers in input_list:
        if int(numbers) > max_number:
            max_number = int(numbers)


    print "The Max number from the input list is",max_number


MaxFinder();

