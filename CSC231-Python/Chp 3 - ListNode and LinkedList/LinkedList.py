#Name: Danielle Rowe
#Date: October 6th, 2020
#Description: Searches through a list looking for a match, then returns the value in the list if there is a match
#   or none if there is not a match (includes a list traversal). 

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

    def append(self, x):
        '''
        insert into the end
        :return:
        '''
        self.insert(len(self), x)
    def prepend(self, x):
        '''
        insert into the front
        :return:
        '''

        self.insert(0, x)

    def pop(self, i=None):
        '''
        removes the ith value from the list. If I is not given removes the
            last value from the list
        :param i (int): Position of the value to remove, zero is the first
        :return: Value removed or none if list is empty
        '''

        if (self.isEmpty()):
            return None
        else:
        # if i is not empty remove the last one
            if i is None:
                i = self.__size - 1

            # Removing the head (or first one in the list)
        if i == 0:
            # save the value before it removes the node
            x = self.__head.getPayLoad()
            # Move the head to the next one
            self.__head = self.__head.getNext()
            # decrement the size
            self.__size -= 1

            # if we just removed the last one from the list,
            # make sure the tail is set to none and so is the head
            if self.__head is None:
                self.__tail = None

                return x

        else:
            # we need to traverse the list until we get to the (i-1)st one.
            previous = self.__getithnode(i - 1)

            # save the value before removing the node
            x = previous.getNext().getPayload()

            # if we happen to be deleting the one at the tail, then we need
            # to move the tail back one position to the previous. But we need to
            # do this before we change the previous.next
            if self.__tail == previous.getNext():
                self.__tail = previous

            # make the (i -1)st point to the (i + 1)st, (skipping the ith)
            previous.setNext(previous.getNext().getNext())

            # decrement the size
            self.__size -= 1

            return x


    def find(self, x):  #find this
        '''
               searches through the list looking for a match, and returns the value in the list if there is a match
               or none if there is not
               :param x (int): Position of the value to remove, zero is the first
               :return: Value removed or none if list is empty
               '''


        current = self.__head
        while current is not None:
            if current.getPayload() == x:
                return current.getPayload()
            current = current.getNext()
        return None

    def __getItem__(self, i):
        '''
        overloads the list index (<e.g. <list>[i]) operator when it is used
        in an expression or in the right hand side of an assignment
        :param i (int): index of all items in a list
        :return: value at ith position in the list
        '''

        return self.__getIthNode(i).getPayload()


    def __setItem__(self, i, value):
        '''
        This overloads the list index (<e.g. <list>[i]) operator when it is used
        in the left hand side of an assignment (e.g. <list>(i) = ...)
        :param i (int): Index of all the items in a list
        :param value: any comparable type
        :return: the value at the ith position of the list
        '''

        self.__getIthNode(i).setPayload(value)



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

    print(newlist.find(8))



#print main function
if __name__ == '__main__':
    main()