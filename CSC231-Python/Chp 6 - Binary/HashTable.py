#Author: Danielle Rowe
#Date: November 10th, 2020
#Description: Uses Hash Table Chaining and Hash Table Probing to insert
# items into a list.

from LinkedList import LinkedList
from Student import Student
import random
import time

class HashTableChaining:
    '''
    Create a Hash Table using Linear Probing for Collision Resolution
    '''

    def __init__(self, size = 17): #not done
        '''
        Constructor
        :param size (int): The size of the table. This should be a prime
        number. The default is 67, which is a pretty small table.
        '''

        #This doesn't work: self.__buckets = [myList()] * self.__size
        # That shortcut only works when create a list of None's or primitive
        # types. It does not work when creating a list of non-primitive
        # types because what it does is create a list of pointers to the
        # same object.

        self.__buckets = []
        for i in range(size):
            self.__buckets.append(LinkedList())

    def __hash(self, value):
        '''
        Hash function
        :param value (any comparable value):
        :return (int): The bucket number for the value
        '''
        return value % len(self.__buckets)

    def insert(self, value):
        '''
        Inserts a value into the hash table
        :param value (any comparable value):
        :return: None
        '''
        bucketNum = self.__hash(value)
        self.__buckets[bucketNum].append(value)

    def find(self, value):
        '''
        Find a value in the table
        :param value (any comparable value):
        :return: Return the value in the table that matches the parameter
        or None if it is not in the table.
        '''
        bucketNum = self.__hash(value)
        result = self.__buckets[bucketNum].find(value)
        return result

    def __str__(self):
        '''
        Create a string representation of the hash table
        :return (string): A string representation of the hash table
        '''
        result = ""
        for i in range(len(self.__buckets)):
            # Put the bucket number in front of each value
            # Each bucket will be in a seperate line
            result += "bucket " + str(i) + ": " + str(len(self.__buckets[i])) + ": "
            result += str(self.__buckets[i]) + "\n"

        return result



class HashTableProbing:
    '''
    Create a Hash Table using Linear Probing for Collision Resolution
    '''
    def __init__(self, size=17): #not done
        '''
        Constructor
        :param size (int): The size of the table. This should be a prime
        number. The default is 67, which is a pretty small table.
        '''

        #This creates a table if size number of "None"'s. This shortcut
        #only works in creatign a list of None's or primitive types.
        #It does not work for non-primitive types because it will instead
        #create a list of size number of pointers that point to the same
        #object.

        self.__buckets = [None] * size
        self.__skip = 3

    def __hash(self, value):
        '''
        Hash function
        :param value (any comparable value):
        :return (int): The bucket number for the value
        '''
        return value % len(self.__buckets)

    def __rehash(self, bucketNum):
        '''
        Re-hash function
        :param bucketNum (int): The last bucekt number attempted
        :return (int): The next bucket number to try
        '''
        return (bucketNum + self.__skip) % len(self.__buckets)

    def insert(self, value):
        '''
        Insert a vlue into the hash table
        :param value (any comparable value):
        :return: None
        '''

        #Hash the value to get the bucket number
        bucketNum = self.__hash(value)

        #Keep the original bucket number so that we know when we have gone
        # completely around the table and need to stop
        originalBucketNum = bucketNum

        # We will first rehash outside of the while loop below because if we dont,
        # then intially, bucketNum and originalBucketNum are the same, so the
        # loop will never execute
        if (self.__buckets[bucketNum] is not None):
            bucketNum = self.__rehash(bucketNum)

        #Keep rehashing until we find an empty bucekt or we have gone all the way
        # around and can't find an empty bucket
        while (self.__buckets[bucketNum] is not None and bucketNum != originalBucketNum):
            bucketNum = self.__rehash(bucketNum)

        #At this point, either we have found an empty bucket, or we have
        # gone all the way around and didn't find an empty bucket because
        # the table is full.
        if (self.__buckets[bucketNum] is None):
            self.__buckets[bucketNum] = value
        else:
            raise Exception("Table Full")

    def find(self, value):
        '''
        Find a value in the table
        :param value (any comparable value):
        :return: Return the value in the table that matches the parameter
        or None if it is not in the table
        '''

        #Hash the value to get the bucket number
        bucketNum = self.__hash(value)

        #Keep the original bucket number so that we know when we have gone
        #completely around the table and need to stop
        originalBucketNum = bucketNum

        # We will first rehash outside of the while loop beloew because if
        # we don't, then initially, bucketNum and originalBucketNum are the
        # same, so the loop will never execute
        if (self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] == value):
            return self.__buckets[bucketNum]

        #keep rehasing until we either find the value or find an empty bucket
        #or we have gone all the way around
        while (self.__buckets[bucketNum] is not None and \
                self.__buckets[bucketNum] != value and \
                bucketNum != originalBucketNum):
            bucketNum = self.__rehash(bucketNum)

        #At this point, either we have found the value we are looking for
        # or we have gone all the way around, or we found an empty bucket.
        # If we found an empty bucket, then the value is not there.
        if (self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] == value):
            return self.__buckets[bucketNum]
        else:
            return None

    def __str__(self):
        '''
        Create a string representation of the hash table
        :return (string): A string representation of the hash table
        '''
        result = ""
        for i in range(len(self.__buckets)):
            # Put the bucket number in front of each value
            # Each bucket will be on a seperate line
            result += "bucket " + str(i) + ": " + str(self.__buckets[i]) + "\n"
        return result

def main():
    HTC = HashTableChaining()
    HTP = HashTableProbing()
    x = 0

    print("Hash Table Probing")
    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]
    for x in values:
        HTP.insert(x)
        print(HTP)

    print("Hash Table Chaining")
    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]
    for x in values:
        HTC.insert(x)
        print(HTC)

#creates the construct
if __name__  == "__main__":
    main()