__author__ = 'egamkar'

def Char_Frequency():
    input = raw_input("Please enter the String to Find its character frquency")

    char_freq_dict = {}

    for char in input:
        if char in char_freq_dict:
            char_freq_dict[char] += 1
        else:
            char_freq_dict[char] = 1


    print char_freq_dict

Char_Frequency()