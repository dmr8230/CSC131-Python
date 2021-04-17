'''
Name: Danielle Rowe
Date: September 17th, 2020
Description: Takes in two files, cross-references the IDs to
see if they match for the different files, and returns the names
if there is a match, and returns that there is not a result
if there is no match.

'''


class Student:
    '''
    Created a new constructor called student
    '''
    def __init__ (self, studentID = None, studentname = ""):
        '''
        Created a constructor
        :param studentID: default None
        :param studentname: default an empty string
        '''
        self.__studentID = studentID
        self.__studentname = studentname


    def getID(self):
        '''
        returns the current studentID
        :parameter self
        :return: the current student ID
        '''
        return self.__studentID
    def getName(self):
        '''
        returns the current student Name
        :parameter self
        :return: the current student Name
        '''
        return self.__studentname
    def setID(self, ID):
        '''
        sets the current studentID to ID
        :param ID: Sets the current student ID to ID
        :return: does not return anything
        '''
        ID = self.__studentID
    def setName(self, name):
        '''
        takes the parameter name, and sets the current student
        to the parameter
        :parameter self and name
        '''
        name = self.__studentname

    def __str__(self):
        '''
        returns a string representation of the student info
        :return: a string representation of the student info
        '''
        return str(self.__studentID) + " " + str(self.__studentname)

    def __cmp__(self, other):
        '''
        compares the current student ID to the past student ID
        returns a negative if the current student is less than the
        other, a postive if its greater, and a 0 if they are equal
        :parameter self and other
        :returns current student - other student
        '''
        return self.__studentID - other.__studentID

    def __eq__(self, other):
        '''
        checks if the self numerator and the other numerator are equal to each other, and if they
        are return True, else return False

        :param other: (fraction)
        :return: True if the numerators are equal, False if they are not
        '''

        if self.__cmp__(other)  == 0:
            return True
        else:
            return False

    def __ne__(self, other):
        '''
        checks if the self numerator and the other numerator are not equal to each other, and if they
        are return True, else return False

        :param other: (fraction)
        :return: True if the numerators are not equal, False if they are not
        '''

        if self.__cmp__(other) != 0:
            return True
        else:
            return False

    def __It__(self, other):
        '''
        checks if the self numerator is smaller than the other numerator, and if they
        are return True, else return False

        :param other: (fraction)
        :return: True if the self numerator is smaller than the other numerator, else return false
        '''

        if self.__cmp__(other) < 0:
            return True
        else:
            return False

    def __le__(self, other):
        '''
        checks if the self numerator is smaller or equal to than the other numerator, and if they
        are return True, else return False

        :param other: (fraction)
        :return: True if the self numerator is smaller or equal to than the other numerator, else return false
        '''

        if self.__cmp__(other) <= 0:
            return True
        else:
            return False

    def __gt__(self, other):
        '''
        checks if the self numerator is larger than the other numerator, and if they
        are return True, else return False

        :param other: (fraction)
        :return: True if the self numerator is larger than the other numerator, else return false
        '''

        if self.__cmp__(other) > 0:
            return True
        else:
            return False

    def __ge__(self, other):
        '''
        checks if the self numerator is greator or equal to the other numerator, and if they
        are return True, else return False

        :param other: (fraction)
        :return: True if the self numerator is greator or equal to the other numerator, else return false
        '''

        if self.__cmp__(other) >= 0:
            return True
        else:
            return False

    def __mod__(self, other):
        if isinstance(other, int):
            return (int(self.__studentID) % other)
        else:
            return int(self.__studentID) % int(other.__studentID)

def main():
    '''
    creates a main function
    :parameter takes no parameters
    :returns prints the name of the IDs that match or else
    says that they do not match
    '''

    #asks for the files to use
    inputfile = str(input("Please enter a list of names file "))
    inputfilehandle = open(inputfile, 'r')

    #intitializes variables to use
    snID = []
    IDnum = 0
    studentname = ""
    for line in inputfilehandle:
        #strip and splits the file, and converts the ID
        #to an integar. Then creates a new Student with
        #the studentname and ID and appends it to the list
        ssline = line.strip(" ").split('\t')
        IDnum = int(ssline[0])
        studentname = ssline[1]
        student = Student(IDnum, studentname)
        snID.append(student)

    #closes the file and sorts it
    inputfilehandle.close()
    snID.sort()

    #asks for a second file, and reads it
    sfile = str(input("Please input the name of the second file "))
    sfilehandle = open(sfile, 'r')

    #creates new variables for the second file
    snID2 = []
    IDnum2 = 0
    for line1 in sfilehandle:
        #strips and splits the second file and adds only the
        #IDs to a new Student
        ssline2 = line1.strip(" ").split('/t')
        IDnum2 = int(ssline2[0])
        student2 = Student(IDnum2)
        found = False
        #compares the IDs from the files and pulls out the
        #name if they match and prints them
        # for j in range(len(snID)):
        #     if student2 == snID[j]:
        #         print(snID[j])
        #         found == True
        #         break

        #creates a new case of the BinarySearch function
        c = binarySearch(snID, student2)
        #if the there is no match for the ID returns that
        if c is None:
            print("No student name matches the student ID:", student2)
        else:
            print(c)
        #if found == False:
            #print("No student name matches the student ID:", student2)

    #sorts and closes the second file
    sfilehandle.close()
    snID2.sort()



def binarySearch(alist, item):
    '''
    This is the binary search algorithm that is used to
    pull out matching IDs by finding the first and last item
    in the list and the midpoint moves these until the number
    is found or the closest case
    :param alist: this is the list
    :param item: this is the specific IDs in the list
    :return: the name of the IDs that match or says if they
    don't match
    '''
    first = 0
    last = len(alist)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
            return alist[midpoint]

        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return None




#creates the construct
if __name__  == "__main__":
    main()

