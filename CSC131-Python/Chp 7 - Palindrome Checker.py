#==========================================================================
# PROGRAM PURPOSE:... Ch7
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I looked up the random.choice(colors) through stack overflow
# WORK TIME(h:mm):... 0:35
#==========================================================================
# Program for Determining Palindromes

import stack

# welcome
print ('This program can determine if a given string is a palindrome\n')
print ('(Enter return to exit)')

# init
char_stack = stack.getStack()
empty_string = ''
longest_pal = '' 

# get string from user
chars = input('Enter string to check: ')


##def countLetters(pal_len):
##    if len(chars) > len(longest_pal):
##        longest_pal = chars
##        print('The new longest palidrome is' , longest_pal) 
##    return len(chars)
##    """ The code above is accepting the string from the user and then
##        counting the number of letters in the string and returning it""" 
    


while chars != empty_string:
    if len(chars) == 1:
        print('A one letter word is by definition a palindrome\n')
        if len(chars) > len(longest_pal):
            longest_pal = chars
            print('The new longest palidrome is' , longest_pal) 
    else:
        # init
        is_palindrome = True
        
        # determine half of length. excluding any middle character
        compare_length = len(chars) // 2

        # push second half of input string on stack
        for k in range(compare_length, len(chars)):
            stack.push(char_stack, chars[k])

        # pop chars and compare to first half of string
        k = 0
        while k < compare_length and is_palindrome:
            ch = stack.pop(char_stack)
            if chars[k].lower() != ch.lower():
                is_palindrome = False
                
            k = k + 1
            
        # display results
        if is_palindrome:
            print (chars, 'is a palindrome\n')
            if len(chars) > len(longest_pal):
                longest_pal = chars
                print('The new longest palidrome is' , longest_pal)  
        else:
            print (chars, 'is NOT a palindrome\n')

    # get string from user
    chars = input('Enter string to check: ')


        
