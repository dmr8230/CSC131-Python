#Name: Danielle Rowe
#Date: September 22nd, 2020
#description : creates a class queue and creates variables between -100 and 100 and
#reads the list backwards and checks it

from Lab5 import LinkedList

class myQueueFrontFirst:
    '''
    creates class Queue to implement Queue ADT
    '''
    def __init__(self):
        '''
        Constructor: start off with an empty queue
        '''
        self.__items = LinkedList()

    def denqueue(self, x):
        '''
        Enqueue an item at the front of the queue
        :param x: item to be queued
        :return: None
        '''

        self.__items.append(x)

    def enqueue(self):
        '''
        dequeue an item from the back of the que
        :return: the item dequeued
        '''

        if (self.isEmpty()):
            return None
        else:
            # pop removes the return items from a list
            # at the position given as an arguement. But we use
            # -1, instead of 0 to return from back of list
            return self.__items.pop(0)

    def peek(self):
        '''
        Return but do not remove the item at the back of the queue.
        :return: the item at the back of the queue
        '''
        if (self.isEmpty()):
            return None
        else:
            #pop won't work here because we don't want to remove the item
            return self.__items[0]

    def __len__(self):
        '''
        overloads the len() operator
        :return:  the number of items in the queue
        '''
        return len(self.__items)

    def isEmpty(self):
        '''
        Returns True if the queue is empty, False if it is not empty.
        :return: True of the queue is empty, false otherwise
        '''
        return len(self.__items) == 0




import random
def main():
    '''
    creates a main function
    :return: tests the len(), isEmpty(), __str__() and prints the values
    '''
    #intializes the Queue function
    theQueue = myQueueFrontFirst()

    #tests that the stack is working as intended
    print("Testing Stack implemented")
    print("theStack is Empty ==", theQueue.isEmpty())
    print("The size of theStack is ", len(theQueue))
    print("The item at the top is ", theQueue.peek())

    #populates the list with values from -100 to 100
    for i in range(10):
        x = random.randint(-100,100)
        print(x)
        theQueue.enqueue(x)

    #tests that the stack is working as intended
    print("theStack is Empty ==", theQueue.isEmpty())
    print("The size of theStack is ", len(theQueue))
    print("The item at the top is ", theQueue.peek())

    #dequeue and print the values of the queue until the
    #queue is empty
    while (not theQueue.isEmpty()):
        x = theQueue.dequeue()
        print("popped the value", x)

    #tests that the stack is working as intended
    print("theStack is Empty ==", theQueue.isEmpty())
    print("The size of theStack is ", len(theQueue))
    print("The item at the top is ", theQueue.peek())

    # This is an extra pop at the end after the Stack has been
    # emptied. This is a check to make sure that pop() on an
    # empty stack does nothing worse than return None.
    print(theQueue.dequeue())
