#! /usr/bin/env python
__author__ = 'egamkar'

def StringLengthFinder():
    input = raw_input("please input the string")

    count = 0

    for char in input:
        count += 1

    print count

StringLengthFinder()
