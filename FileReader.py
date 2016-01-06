import string

__author__ = 'egamkar'

file_name = "assignment.txt"


def file_reader():
    fopen = open(file_name,'r')
    content = fopen.readlines()
    count = 0
    message = ''
    for lines in content:
        message += lines[count%40]  # message = message + lines[count%40]
        count += 1
    fopen.close()
    print message


file_reader()
