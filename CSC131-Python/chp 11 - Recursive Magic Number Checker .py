#==========================================================================
# PROGRAM PURPOSE:... Ch11 - Recursive Magic Number Checker
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I looked up some of the syntax online, and one of the tutor helped me with a few computing errors 
# WORK TIME(h:mm):... 1:30
#==========================================================================

# first answer for user input
print("Select a lower limit, upperlimit, and magic number")
x = False 
while x == False: 
    try:
        lowerlim = int(input("Lower Limit: "))
        upperlim = int(input("Upper Limit: "))
        magicnum = int(input("Magic Number: "))
        x = True 
    except:
        print("You must input integers, please try again")
        
# needs a while loop to ensure magic num is between limits
    
while lowerlim>upperlim:
    print("Your lower limit must be less than your upper limit please try again")
    lowerlim = int(input("Lower Limit: "))
    upperlim = int(input("Upper Limit: "))
while magicnum>upperlim or magicnum<lowerlim:
    magicnum = int(input("Magic number music be > ", lowerlim, " and < ", upperlim, ". Choose another magic number: "))

guess = 0 

# create the recursive checker that should check itself 

def magicnumcheck(upperlim1,lowerlim1,magicnum1): 

    """ This function uses recursion to go through numbers between the limits
        given in order to find the magic number"""
    
    
    guess = (upperlim1 - lowerlim1)// 2 + lowerlim1

    #create a while loop that quits once the magic number is found
    
    # next check if the code is higher or lower than the guess
    if guess > magicnum1:
        # you will need to subtract the previous guess from the
        # current guess divided by 2
        # with a // 2 to make sure that its not a fraction
        upperlim1 = guess
        
        print("Guess is ", guess, " ... Lower")
        magicnumcheck(upperlim1, lowerlim1, magicnum1)
    elif guess < magicnum1:
        lowerlim1 = guess 
        print("Guess is ", guess, " ... Higher")
        magicnumcheck(upperlim1, lowerlim1, magicnum1) 

    else:
        print("Guess is ", guess, "... Winner")


guess1 = upperlim // 2

magicnumcheck(upperlim, lowerlim, magicnum) 


    
