# author: Dani Rowe
# date: November 24th, 2020
# description: implements bubble sort, selection sort, and insertion sort

import random

def swap(theList, i, j):
    '''
    Swaps the values in the list at positions i and j
    :param theList:
    :param i (int):
    :param j (int):
    :return: None
    '''
    temp = theList[i]
    theList[i] = theList[j]
    theList[j] = temp

def bubbleSort(theList):
    '''
    Sorts by using the Bubble Sort algorithm
    :param theList: a list of comparable values not sorted
    :return: None
    '''
    N = len(theList)
    i = N-1
    stopEarly = False

    while i>0 and not stopEarly:
        stopEarly = True

        for j in range(0, i):
            if theList[j] > theList[j+1]:
                swap(theList, j, j+1)
                stopEarly = False
        i -= 1

def selectionSort(theList):
    '''
    Sorts by using the Selection Sort algorithm
    :param theList: a list of comparable values not sorted
    :return: None
    '''

    N = len(theList)

    for i in range(N-1):
        smallestPosition = i
        for j in range(i + 1, N):
            if theList[smallestPosition] > theList[j]:
                smallestPosition = j

        swap(theList, i, smallestPosition)

def insertionSort(theList):
    '''
    Sorts by using the Insertion Sort algorithm
    :param theList: a list of comparable values not sorted
    :return: None
    '''

    N = len(theList)

    for i in range(1, N):
        holdValue = theList[i]
        j = i
        while j > 0 and theList[j-1] > holdValue:
            theList[j] = theList[j-1]
            j -= 1
        theList[j] = holdValue

def main():
    #testing the bubble sort
    myList = [random.randint(1,100) for i in range(30)]

    print("The sorted list = " + str(sorted(myList)))
    print("The unsorted list = " + str(myList))
    print("")
    bubbleSort(myList)
    print("After bubble sort = " + str(myList))

    #gap for aesthetic
    print("")
    print("")

    #testing the selection sort
    myListS = [random.randint(1,100) for i in range(30)]

    print("The sorted list = " + str(sorted(myListS)))
    print("The unsorted list = " + str(myListS))
    print("")
    selectionSort(myListS)
    print("After Selection sort = " + str(myListS))

    #gap for aesthetic
    print("")
    print("")

    #testing the insertion sort
    myListI = [random.randint(1,100) for i in range(30)]

    print("The sorted list = " + str(sorted(myListI)))
    print("The unsorted list = " + str(myListI))
    print("")
    insertionSort(myListI)
    print("After Insertion sort = " + str(myListI))

#creates the construct
if __name__  == "__main__":
    main()