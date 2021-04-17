#==========================================================================
# PROGRAM PURPOSE:... Ch7-2 CSC131 Homework Helper Module 
# AUTHOR:............ Rowe, Danielle
# COURSE:............ CSC 131-006
# TERM:.............. Spring 2019
# COLLABORATION:..... I looked at past code for referencing 
# WORK TIME(h:mm):... 1:30
#==========================================================================

import turtle as t
import sys


def makeGrid(width, height, blocksize, turtleobject):
    """"Draws a grid with the turtle object as the worker accepting the parameters given"""

    heightdis = (800-height)/2
    startposheight = -400 + heightdis
    widthdis = (800-width)/2
    startposwidth = -400 + widthdis
    nbrlines = 0
    

    while nbrlines <=  width/blocksize:

        while startposwidth < width/2:
            
            t.penup()
            t.setposition(startposwidth, startposheight)
            startposwidth += width
            t.pendown()
            t.setposition(startposwidth, startposheight)
            t.penup()
            
        startposheight += blocksize
        nbrlines += 1
        startposwidth = -400 + widthdis

    nbrlines = 0
    startposheight = -400 + heightdis
    startposwidth = -400 + widthdis

    while nbrlines <= height/blocksize:

        while startposheight < height/2:

            t.penup()
            t.setposition(startposwidth, startposheight)
            startposheight += height
            t.pendown()
            t.setposition(startposwidth, startposheight)
            t.penup()

        startposwidth += blocksize
        nbrlines += 1
        startposheight = -400 + heightdis

        
    
        


def userInputInt(lowerlimit, upperlimit):
    """Prompt the user for input of an integer between the limits given, then return
        the valid input as a return value"""
    print("The lower limit is", lowerlimit, "and the upper limit is", upperlimit) 
    userinput = int(input("Give a number between these limits "))
    while userinput > upperlimit or userinput < lowerlimit:
        userinput = int(input("Please, enter a number between these limits "))
    return userinput

def getFile():
    """Prompt the user for the file name of the file which holds the cipher text"""
    filename = False
    fname = input("File name: ")
    while filename == False:
        try:
            ifile = open(fname, 'r')
            filename = True
        except:
            print("Could not find file.")
            fname = input("Incorrect file name, please re-enter:") 
            #sys.exit()
    
        
    # use exception in order to catch the error and reprompt user for file name
    
        # Read the whole file
        # While loop that ends at last line of file (re-use while loop logic)
        # Declare all counter variables like a_count int, b_count int,
        # Each letter that is read needs to be counted uniquely
           # array from w3resouce
        # Sort the arrry so they are biggest to smallest
    #  Read teh file again top to bottom
    #  For each letter map to the one in the array and then next step
        # Use the position of the value in the array to map to the cipher and printout a letter
        
     
    return fname, ifile


