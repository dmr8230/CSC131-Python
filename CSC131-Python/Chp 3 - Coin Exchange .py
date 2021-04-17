#==========================================================================
# PROGRAM PURPOSE:... Ch3 M7 Coin Change Exercise Program: Raising the Challenge
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I went to the stem lab, and went to Mr. Stoker's office hours for help
# WORK TIME(h:mm):... 1:10
#==========================================================================



# Coin Change Exercise Program

import random

# program greeting
print('The purpose of this exercise is to enter a number of coin values')
print('that add up to a displayed target value.\n')
print('Enter coins values as 1-penny, 5-nickel, 10-dime and 25-quarter')
print("Hit return after the last entered coin value.")
print('----------------')

# init
terminate = False
empty_str = ''

# start game
while not terminate:
    amount = random.randint(1,99)
    print('Enter coins that add up to', amount, 'cents, one per line. The least possible number of coins should be entered \n')
    game_over = False
    total = 0
    q = 0
    d = 0
    n = 0
    p = 0
    userq = 0
    userd = 0
    usern = 0
    userp = 0
    amount2 = amount

    
    while (amount - 25 >= 0):
        amount = amount - 25
        q = q + 1
    while (amount - 10 >= 0):
        amount = amount - 10
        d = d + 1
    while (amount - 5 >= 0):
        amount = amount - 5
        n = n + 1
    while (amount - 1 >= 0):
        amount = amount - 1
        p = p + 1
    amount = amount2
    
    while not game_over:
        valid_entry = False
        
        
        while not valid_entry:


                    
            if total == 0:
                entry = input('Enter first coin: ')

                if (entry == '25'):
                    userq = userq + 1
                if (entry == '10'):
                    userd = userd + 1
                if (entry == '5'):
                    usern = usern + 1
                if (entry == '1'):
                    userp = userp + 1
                    
                
            else:
                entry = input('Enter next coin: ')

                if (entry == '25'):
                    userq = userq + 1
                if (entry == '10'):
                    userd = userd + 1
                if (entry == '5'):
                    usern = usern + 1
                if (entry == '1'):
                    userp = userp + 1
                
            if entry in (empty_str,'1','5','10','25'):
                valid_entry = True
            else:
                print('Invalid entry')
        
        if entry == empty_str:
            if total == amount:
                if (q == userq and d == userd and  n == usern and p == userp):
                    print('Correct! you have entered the correct amount with the least possible number of coins to be entered')
                else:
                    print("You have entered the correct amount, but you did not enter the least possible number of coins")
                          
            else:
                print('Sorry - you only entered', total, 'cents.')
                
            game_over = True
            
        else:
            total = total + int(entry)
            if total > amount:
                print('Sorry - total amount exceeds', amount, 'cents.')
                game_over = True
                
        if game_over:
            entry = input('\nTry again (y/n)?: ')
            
            if entry == 'n':
                terminate = True

print('Thanks for playing ... goodbye')
    


