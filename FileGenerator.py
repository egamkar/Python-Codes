import random
import string

__author__ = 'egamkar'

file_name = "assignment.txt"


def file_writer():
    fopen = open(file_name,'w')
    message = "Welcome to Python KT Assignment.Congratulations for reaching till this time.Hope you are doing fine"
    count = 0
    for char in message:
        chars = "".join([random.choice(string.letters) for i in xrange(40)])
        final_chars = chars[:(count%40)]+char+chars[(count%40)+1:]
        fopen.write(final_chars+'\n')
        count += 1
    fopen.close()


file_writer()
