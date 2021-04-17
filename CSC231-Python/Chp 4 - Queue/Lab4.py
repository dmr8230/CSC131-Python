#Name: Danielle Rowe
#Date: September 22nd, 2020
#description : creates a class queue and creates variables between -100 and 100 and
#reads the list backwards and checks it

class Queue:
    '''
    creates class Queue to implement Queue ADT
    '''
    def __init__(self):
        '''
        Constructor: start off with an empty queue
        '''
        self.__queueitems = []

    def enqueue(self, x):
        '''
        Enqueue an item at the front of the queue
        :param x: item to be queued
        :return: None
        '''

        self.__queueitems.insert(0,x)

    def dequeue(self):
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
            return self.__queueitems.pop()

    def peek(self):
        '''
        Return but do not remove the item at the back of the queue.
        :return: the item at the back of the queue
        '''
        if (self.isEmpty()):
            return None
        else:
            #pop won't work here because we don't want to remove the item
            return self.__queueitems[-1]

    def __len__(self):
        '''
        overloads the len() operator
        :return:  the number of items in the queue
        '''
        return len(self.__queueitems)

    def isEmpty(self):
        '''
        Returns True if the queue is empty, False if it is not empty.
        :return: True of the queue is empty, false otherwise
        '''
        return len(self.__queueitems) == 0


class Stack:
    '''
    creates class Stack to implement a Stack ADT
    '''
    def __init__(self):
        '''
        creates constructor to intialize the list
        :parameter takes parameter self
        :returns nothing
        '''
        self.__items = []

    def push(self, x):
        '''
        appends item x to the items list
        :param x: take in random input
        :return: nothing
        '''
        self.__items.append(x)

    def pop(self):
        '''
        makes sure self is not empty, else uses pop to delete last var
        :return: None if empty, last value if not
        '''
        if (self.isEmpty()):
            return None
        else:
            return self.__items.pop()

    def peek(self):
        '''
        returns but does not remove the item at the front of the queue
        if the list is empty
        :return: None if list is empty, front of queue if it is
        '''
        if (self.isEmpty()):
            return None
        else:
            return self.__items[len(self)-1]

    def __len__(self):
        '''
        gives the length of the list
        :return: the length of the list
        '''
        return len(self.__items)

    def isEmpty(self):
        '''
        checks to see if the list is empty
        :return: if the list is empty (or equal to 0)
        '''
        return len(self) == 0

#imports random so can be used to populate the list
import random

#creates the function main
def main():
    #intializes the Queue function
    theQueue = Queue()

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

#creates the function main
def main2():
    #intializes the Queue function
    theStack = Stack()

    #tests that the stack is working as intended
    print("Testing Stack implemented")
    print("theStack is Empty ==", theStack.isEmpty())
    print("The size of theStack is ", len(theStack))
    print("The item at the top is ", theStack.peek())

    #populates the list with values from -100 to 100
    for i in range(10):
        x = random.randint(-100,100)
        print(x)
        theStack.push(x)

    #tests that the stack is working as intended
    print("theStack is Empty ==", theStack.isEmpty())
    print("The size of theStack is ", len(theStack))
    print("The item at the top is ", theStack.peek())

    #dequeue and print the values of the queue until the
    #queue is empty
    while (not theStack.isEmpty()):
        x = theStack.pop()
        print("popped the value", x)

    #tests that the stack is working as intended
    print("theStack is Empty ==", theStack.isEmpty())
    print("The size of theStack is ", len(theStack))
    print("The item at the top is ", theStack.peek())

    # This is an extra pop at the end after the Stack has been
    # emptied. This is a check to make sure that pop() on an
    # empty stack does nothing worse than return None.
    print(theStack.pop())

#creates main that is working with stack instead of queue
if __name__ == "__main__":
    main()

