# Author: Dani Rowe
# Date: November 17th, 2020
# Description: Implements the Heap ADT, then adds values to the heap
# displays the added values and then deletes them in order

import random

class minHeap:
    def __init__(self):
        '''
        Constructor
        '''

        # The size is one less than the len. So we can't use
        # len(self.__theHeap). But we can just keep a tally of the number
        # of value in the heap
        self.__size = 0

        #This is not an empty list. It is a list with one thing in it that
        # happens to be "none"
        self.__theHeap = [None]

    def __len__(self):
        '''
        Overloads the len operator
        :return: The number of values in the heap
        We cannot just return len(self.__theHeap) because there is the "None"
        in the first cell. Would could just return len(self.__theHeap) + 1
        but I think just keepign a tally is less confusing for students
        '''
        return self.__size

    def __getParent(self, i):
        '''
        Get the position of the parent of the node i
        :param i (int): a position of a node
        :return (int): the position of the parent of node i
        '''
        return i //2

    def __getLeftChild(self, i):
        '''
        get the position of the left child of node i
        :param i (int): a position of a node
        :return (int): the position of the left child of node i
        '''
        return i * 2

    def __getRightChild(self,i):
        '''
        Get the position of the right child of node i
        :param i (int): a position of a node
        :return (int): The position of the left right of node i
        '''
        return i * 2 + 1

    def isEmpty(self):
        '''
        Returns True if the heap is empty, false otherwise.
        :return (boolean): Returns True if the heap is empty, false otherwise.
        '''
        return self.__size == 0

    def insert(self, x):
        '''
        Inserts a value into the heap
        :param x (any comparable value):
        :return: None
        '''

        self.__size += 1
        self.__theHeap.append(x)
        self.__percolateUp(self.__size)

    def deleteMin(self):
        '''
        Removes and returns the minimum value in the heap.
        :return (comparable value): Returns the minimum value in the heap
        '''

        # Save the value at the root
        if self.__size < 1:
            return None
        value = self.__theHeap[1]

        # Mvoe the last value into the 1st position and decrement the size
        self.__theHeap[1] = self.__theHeap[self.__size]

        #Remove the last value from the list
        self.__size -= 1
        self.__theHeap.pop()

        #percolate the new value at 1 (which is a large value) down.
        self.__percolateDn(1)
        return value

    def __percolateUp(self, i):
        '''
        Percolates up starting at position i
        :param i (int): a position in the heap
        :return: None
        '''
        parent = self.__getParent(i)
        # If the parent of i is zero, then i IS the root and we are done
        while(parent > 0):
            # Swap if the parent values is bigger than the child
            # WE stop the whole process once we stop swapping.
            if (self.__theHeap[parent] > self.__theHeap[i]):

                self.__swap(parent, i)

                # This move us up. WE set i to the parent, then get the parent again,
                # which would then be the grandparent, moving everthing up to the
                # next level
                i = parent
                parent = self.__getParent(i)
            else:
                parent = 0 # stops the loop

    def __percolateDn(self, i):
        '''
        Recolates down starting at position i
        :param i (int): A position in the heap
        :return: None
        '''

        lChild = self.__getLeftChild(i)
        rChild = self.__getRightChild(i)

        # Because a Heap is a complete tree, if there is no left child, then
        # there is no right child either, so we don't have to check for that.
        # if there is at least a left child, then we COULD percolate.
        while (lChild <= self.__size):

            # Which child is bigger?
            # If we don't have a right child, then min will be the left child
            # But if we do have a right child, then min will be the smaller of
            # of the two children

            min = lChild
            if(rChild <= self.__size and self.__theHeap[rChild] < self.__theHeap[lChild]):
                min = rChild

            # Assertion: min is the smaller of the two children if they exist

            if (self.__theHeap[i] > self.__theHeap[min]):
                self.__swap(i, min)
                # This moves down the tree. We set i to be the child we just swapped
                # with, then recompute the locations of the left and right children.
                i = min
                lChild = self.__getLeftChild(i)
                rChild = self.__getRightChild(i)
            else:
                # Once we don't swap, then we are done.
                lChild = self.__size + 1 # stops the loop
                # or break

    def __swap(self, i, j):
        '''
        takes the two positions as parameters and switches the values
        in the Heap at the two positions
        :return: None
        '''
        self.__theHeap[i], self.__theHeap[j] = self.__theHeap[j], self.__theHeap[i]

    def __str__(self):
        '''
        returns a string represntation of the values in the Heap
        :param self:
        :return: the string representation of the values in the Heap
        '''
        result = ""
        for x in range(1, len(self.__theHeap)):
            result += "\nParent value: " + str(self.__theHeap[x])
            if 2 * x < len(self.__theHeap) :
                result += " Left Child: " + str(self.__theHeap[2 * x])
            if 2 * x + 1 < len(self.__theHeap) :
                result += " Right Child: " + str(self.__theHeap[2 * x + 1])

        return result

def main():
    MH = minHeap()

    MH.isEmpty()
    print("The length is: " , len(MH))
    print("The str function is: " + str(MH))

    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10, 17, 202, 195, 34, 87]
    for x in values:
        MH.insert(x)

    print(MH)

    MH.isEmpty()
    print("The length is: " , len(MH))
    print("The str function is: " + str(MH))

    for x in values:
        delMH = MH.deleteMin()
        print("The value you are deleting is: " + str(delMH))

    print(MH)

    MH.isEmpty()
    print("The length is: " , len(MH))
    print("The str function is: " + str(MH))



#creates the construct
if __name__  == "__main__":
    main()
