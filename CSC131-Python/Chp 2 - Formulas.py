#==========================================================================
# PROGRAM PURPOSE:... Ch2 P5 entering two integer values and completing formulas 
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... Went to the STEM lab and he explained floating-point
# results and how you get them 
# WORK TIME(h:mm):... 0:20
#==========================================================================

firstint = int(input('Enter an integer '))
secondint = int(input('Enter a second integer '))

addition = firstint + secondint 
print(firstint , '+' , secondint, '=' , addition) 

subtraction = firstint - secondint 
print(firstint , '-' , secondint , '=' , subtraction)

multiplication = firstint * secondint
print(firstint , '*' , secondint , '=' , multiplication)

division = format(firstint/secondint, '.2f')
print(firstint , '/' , secondint , '=' , division)

doubledivision = firstint//secondint
print(firstint , '//' , secondint , '=' , doubledivision)

remainder = firstint%secondint
print(firstint , '%' , secondint , '=' , remainder)

doublemultiplication = format(firstint**secondint, ',.2f')
print(firstint , '**' , secondint , '=' , doublemultiplication)



