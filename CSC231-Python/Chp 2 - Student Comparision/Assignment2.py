'''
Author: Dani Rowe
Date: October 15, 2020
Description: Searches through the code using a linked list, and first
inserts the code into the list, then searches through the list and finds
the name ID match and gives the name. 
'''

#import time, student, and linkedlist
from LinkedList import LinkedList
from Assignment1 import Student
import time


def main():
    #open the list of names file and read the student info then put it into a list
    inputfile = str(input("Please enter a list of names file "))
    inputfilehandle = open(inputfile, 'r')
    inputfileread = inputfilehandle.readlines()
    #create a new linkedlist
    llinfo = LinkedList()

    # create a start time for the creater
    starttime = time.time()

    #create a for loop that strips and splits the linked list then adds the items to it
    for line in inputfileread:
        ssline = line.strip(" ").split('\t')
        #changes the variable to an int
        ssline[0] = int(ssline[0])
        #inserts the values into the linked list
        llinfo.append(Student(ssline[0], ssline[1]))

    # closes the file
    inputfilehandle.close()
    #create an end time
    endtime = time.time()

    # asks for a second file, and reads it
    sfile = str(input("Please input the name of the second file "))
    sfilehandle = open(sfile, 'r')
    Idsearch = sfilehandle.readlines()
    #start time for the searcher
    starttime2 = time.time()

    # loop through the second list to compare the two
    for IDcomparison in Idsearch:
        #change it to an integar
        IDcomparison = int(IDcomparison)
        studentID = Student(IDcomparison)

        #finds the cross-over
        IDchecker = llinfo.find(studentID)
        #checks to see if the ID was found or not and prints it
        if IDchecker is not None:
            print("Found student record "  + str(IDchecker))
        else:
            print("Student ID " + str(IDcomparison) + " not found")

    endtime2 = time.time()
    #print the time it takes to run and search through the code
    print("Time to insert " + format(endtime-starttime, "6.4f") + " seconds.")
    print("Time to search through " + format(endtime2 - starttime2, "6.4f") + " seconds.")




    #sorts and closes the second file
    sfilehandle.close()

#creates the construct
if __name__  == "__main__":
    main()
