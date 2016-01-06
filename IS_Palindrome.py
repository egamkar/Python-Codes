__author__ = 'egamkar'

def IS_Palindrome():
    input = raw_input("please enter the input string for checking palindrome")

    is_palindrome = True

    count = 0
    reverse_count = len(input)

    for char in input:
        reverse_count -= 1
        if input[count] != input[reverse_count]:
            is_palindrome = False
        count += 1


    if is_palindrome:
        print "The Entered Input is a Palindrome"
    else:
        print "The Entered Input is not a palindrome"


IS_Palindrome()
