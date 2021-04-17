# Author: Dani Rowe
# Date: November 24th, 2020
# Description: Inserts and searches through the list using Hash Table Chaining and
# and Hash Table Probing then times how long each takes 

from LinkedList import LinkedList
from Assignment1 import Student
from HashTable import HashTableChaining
from HashTable import HashTableProbing
import time

def main():
    #tablesize = 800001

    #for probing

    primeNumbers = (750019, 740011,730003, 720007) #, 710009, 700001, 690037,
                   # 680003, 670001, 660001, 650011, 640007, 630017, 620003)

    #for chaining
    #primeNumbers = (100003, 90001) # 80021, 70001, 60013, 50021, 40009, 30011, 20011, 10007)

    #this is the names of the files
    inputfile2 = "searchIds_short.txt"
    inputfile = "listOfNames_short.txt"

    for tableSize in primeNumbers:
        probingHT = HashTableProbing(tableSize)
        #ChainingHT = HashTableChaining(tableSize)

        # open the list of names file and read the student info then put it into a list
        inputfilehandle = open(inputfile, 'r')
        inputfileread = inputfilehandle.readlines()

        #startTime to insert names and IDs
        startTime = time.time()

        for line in inputfileread:
            ssline = line.strip(" ").split('\t')
            #changes the variable to an int
            sID = int(ssline[0])
            sname = ssline[1]
            student1 = Student(sID, sname)
            probingHT.insert(student1)
            #ChainingHT.insert(student1)

        #endtime to insert names and IDs
        endTime = time.time()
        inputfilehandle.close()

        # asks for a second file, and reads it
        sfilehandle = open(inputfile2, 'r')
        Idsearch = sfilehandle.readlines()

        #starttime to search through the student records
        startTime2 = time.time()

        # search for an ID match in the search file and BinarySearchTree
        for ID in range(len(Idsearch)):
            num = Idsearch[ID]
            # change it to an integar
            IDcomparison = int(num)
            studentID = Student(IDcomparison)
            #finds the cross-over
            Tester = probingHT.find(studentID)
            #Tester = ChainingHT.find(studentID)
            #checks to see if the ID was found or not and prints it
            current = 0
            # print("You are searching for this ID: " , studentID)
            # if Tester is None:
            #     print("The ID was not found (using HashTableChaining): "  + str(studentID))
            #     print("The ID was not found (using HashTableProbing): " + str(studentID))
            # else:
            #     print("This was the ID found (using HashTable Chaining): " + str(Tester))
            #     print("This was the ID found (using HashTableProbing): " + str(Tester))

        #create a start time for the creater
        sfilehandle.close()

        #endtime to search through the student records
        endTime2 = time.time()

        #print("Time to insert the Names and IDs using HashTableChaining: ", endTime - startTime, " seconds")
        #print("Time to search through the student records using HashTableChaining: ", endTime2 - startTime2, " seconds")
        print("Time to insert the case ", tableSize, " the Names and IDs using HashTableProbing: ", endTime - startTime, " seconds")
        print("Time to search through the case " , tableSize, " the student records using HashTableProbing: ", endTime2 - startTime2, " seconds")


#creates the construct
if __name__  == "__main__":
    main()