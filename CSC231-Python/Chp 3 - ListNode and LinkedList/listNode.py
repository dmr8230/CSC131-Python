#Name: Danielle Rowe
#Date: September 29th, 2020
#Description: Creates a listNode and LinkedList, and then adds items
#             to the beginning, middle, and end of the list

class listNode:
    '''
    This is the class for the lsit nodes, which form the change. The
    listNode's contain the payload
    '''

    def __init__(self, payload = None, next = None):
        '''
        Constructor
        :param payload: Any type that is comparable
        :param next (listNode): the listNode that follows. None if
        this is the last node in the list
        '''

        self.__payload = payload
        self.__next = next

    def getPayload(self):
        '''
        returns the payload
        :param self:
        :return: the current payload
        '''
        return self.__payload

    def setPayload(self, payload):
        '''
        this sets the payload in the input to the self payload
        :param payload: the payload inputed
        :return: none
        '''
        self.__payload = payload

    def getNext(self):
        '''
        returns the Next item
        :param self:
        :return: the next item
        '''
        return self.__next

    def setNext(self, next):
        '''
        this sets the next to the input of the next item
        :param self:
        :param next: the next inputed
        :return: none
        '''
        self.__next  = next


class LinkedList:
    '''
    implements a linked list
    '''
    def __init__(self):
        '''
        constructor: an empty list has no head or tail node and the size
        is zero
        '''
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __getIthNode(self, i):
        '''
        Returns the listNode at the ith position in the list where
        the first node is at position zero. Negative values count backwards
        from the end of the list. Any value >= len(thelist) will end in an
        IndexError.
        :param i (int): the position in the list
        :return: the listNode at the ith position
        :raises IndexError if the index is >= len
        '''

        if i < 0:
            # Negatives count backwards from the end of the list just
            # like with Python lists
            i = self.__size + 1
        elif i >= self.__size:
            raise IndexError ('list index out of range')

        current = self.__head
        count = 0

        #this is called a list traversal
        while current is not None and count < i:
            count += 1
            current = current.getNext()

        return current

    def insert(self, i, x):
        '''
        Inserts x into the list at position i
        :param i (int): Position to insert x. 0 is before the 1st
                        1 is after the first values but before the
                        a value >= len is appended to the list
        :param x: Any type that is comparable
        :return None
        '''

        #list is the empty, i doesn't matter.
        if self.isEmpty():
            self.__head = listNode(x)
            self.__tail = self.__head

        # inserting before the head
        elif i <= 0:
            self.__head = listNode(x, self.__head)

        #inserting after the tail
        elif i >= self.__size:
            self.__tail.setNext(listNode(x))
            self.__tail = self.__tail.getNext()

        #inserting someplace in between
        else:
            #we need to traverse the list until we get to the (i-1)st one.
            previous = self.__getIthNode(i-1)
            previous.setNext(listNode(x, previous.getNext()))
            if (self.__tail == previous):
                self.__tail = self.__tail.getNext()
        self.__size += 1


    def front(self):
        '''
        returns the value at the front of the list
        :return: the value at the front of the list or None if the
                 list is empty
        '''
        if self.isEmpty():
            return None
        else:
            return self.__head.getPayload()

    def back(self):
        '''
        returns the value at the back of the list
        :return: returns the value at the back of the lisst or None
                 if the list is empty
        '''
        if self.isEmpty():
            return None
        else:
            return self.__tail.getPayload()

    def __len__(self):
        '''
        Overloads the len operator
        :return: the size of the list
        '''
        #By keeping track of the size as we go, we don't have to
        #count the number of nodes, which would be O(N)
        return self.__size

    def isEmpty(self):
        '''
        returns true if the list is empty
        :return: true if the list is empty, false otherwise
        '''
        #could return self.__size == 0
        return self.__head is None

    def __str__(self):
        '''
        returns a string of the values in the list. This required that
        str() can be applied to the items in the list.
        :return returns a string of the values in the list
        '''

        result = ""
        current = self.__head
        while current is not None:
            result = result + " " + str(current.getPayload())
            current = current.getNext()
        return result

def main():
    '''
    creates a main function
    :return: tests the len(), isEmpty(), __str__() and prints the values
    '''
    newlist = LinkedList()
    print("Test for len(): " , len(newlist))
    print("Test for isEmpty: " , newlist.isEmpty())
    print("Print the list: " , newlist)
    print()

    #insert into front
    newlist.insert(0,12)
    print("Test for len(): " , len(newlist))
    print("Test for isEmpty: " , newlist.isEmpty())
    print("Print the list: " , newlist)
    print()

    #insert into back
    newlist.insert(1000, 2)
    print("Test for len(): ", len(newlist))
    print("Test for isEmpty: ", newlist.isEmpty())
    print("Print the list: ", newlist)
    print()

    #insert into middle
    newlist.insert(2, 10)
    print("Test for len(): ", len(newlist))
    print("Test for isEmpty: ", newlist.isEmpty())
    print("Print the list: ", newlist)
    print()

    #insert into middle
    newlist.insert(5, 15)
    print("Test for len(): ", len(newlist))
    print("Test for isEmpty: ", newlist.isEmpty())
    print("Print the list: ", newlist)
    print()

    #insert into middle
    newlist.insert(8, 8)
    print("Test for len(): ", len(newlist))
    print("Test for isEmpty: ", newlist.isEmpty())
    print("Print the list: ", newlist)
    print()

    #re-test len() and isEmpty()
    print("Test for len(): ", len(newlist))
    print("Test for isEmpty: ", newlist.isEmpty())
    print("Print the list: ", newlist)
    print()



#print main function
if __name__ == '__main__':
    main()




