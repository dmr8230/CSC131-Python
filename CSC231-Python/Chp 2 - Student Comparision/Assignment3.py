# Author: Danielle Rowe
# Date: November 12th, 2020
# Description: Searches through using the Binary Search Tree to first insert
# the IDs in, and then uses a find with all of the SearchIDs

#grab all of the classes and functions we need from the different programs
from BinarySearch import BinarySearch
from BinarySearchTree import BinarySearchTree
from AVLTrees import AVLTree
from Assignment1 import Student
import time

def main():
    #open the list of names file and read the student info then put it into a list
    inputfile = str(input("Please enter a list of names file "))
    inputfilehandle = open(inputfile, 'r')
    inputfileread = inputfilehandle.readlines()
    # BST = BinarySearchTree()
    BST = BinarySearchTree()

    #loops through and adds Student record to BinarySearchTree

    #create a start time for the creater
    starttime = time.time()

    #find out how many records your inserting into
    insertrecordcounter = 0

    for line in inputfileread:
        ssline = line.strip(" ").split('\t')
        #changes the variable to an int
        sname = int(ssline[0])
        BST.insert(Student(sname))
        insertrecordcounter += 1

    inputfilehandle.close()
    endtime = time.time()
    print(BST)

    #create a start time for the creater


    # asks for a second file, and reads it
    inputfile2 = str(input("Please enter a list of names file "))
    sfilehandle = open(inputfile2, 'r')
    Idsearch = sfilehandle.readlines()

    #create a start time for the creater
    starttime2 = time.time()

    findrecordcounter = 0
    # search for an ID match in the search file and BinarySearchTree
    for ID in range(len(Idsearch)):
        findrecordcounter += 1
        num = Idsearch[ID]
        # change it to an integar
        IDcomparison = int(num)
        studentID = Student(IDcomparison)
        #finds the cross-over
        IDchecker = BST.find(studentID)
        #checks to see if the ID was found or not and prints it
        if IDchecker is not None:
            print("Found student record "  + str(IDchecker))
        else:
            print("Student ID " + str(IDcomparison) + " not found")
    #create a start time for the creater
    sfilehandle.close()
    endtime2 = time.time()

    print("Time to insert " + str(insertrecordcounter) + " records into an AVL Tree: " + format(endtime-starttime, "6.4f") + " seconds")
    print("Time to find " + str(findrecordcounter) + " records into an AVL Tree: " + format(endtime2-starttime2, "6.4f") + " seconds")

    # RESULTS: These results tell us that the AVL Tree took more time to run
    # than the Binary Search Tree, and the sorted takes longer on the Binary Search
    # tree than the unsorted. However, the sorted time is less for the AVL Trees
    # I gave the data below for reference
    # Table of Values Binary Search Table:
    #     Short Time: .008 and .009
    #     Sorted Time: 044 and .041
    #     Medium Time: .508 and .38
    #     Long Time: 34.68 and 26.95
    #     Long Time Sorted: N/A recursion limit is reached
    # Table of Values for AVL:
    #     Short Time: .012 and .008
    #     Sorted Time: .006 and .007
    #     Medium Time: .53 and .29
    #     Long Time: 45.03 and 21.12

#creates the construct
if __name__  == "__main__":
    main()