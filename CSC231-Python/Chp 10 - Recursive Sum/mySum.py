'''
Author: Dani Rowe
Date: October 13th, 2020
Description: This program implements a recursive sum operation on a list
'''
import random
def recSum1(someList):
    '''
    this function adds all the items in the list together
    :param someList: takes the list
    :return: the sum of the function
    '''
    if len(someList) == 1:
        return someList[0]

    else:
        a = recSum1(someList[:len(someList) //2])
        b = recSum1(someList[len(someList) // 2:])
        return a + b


def recSum2(someList):
    '''
    Takes the sum of the funciton and adds it together
    :param someList: the list
    :return: all of the items added together
    '''
    if len(someList) == 1:
        return someList[0]

    else:
        return someList[0] + recSum2(someList[1:])

def minvalues(someList):
    '''
    finds the minimum value in the function
    :param someList: the list
    :return: the minimum value in the list
    '''
    if len(someList) == 1:
        return someList[0]
    else:
        firsthalf = minvalues(someList[:len(someList) //2])
        secondhalf = minvalues(someList[len(someList) //2:])
        if (firsthalf < secondhalf):
            return firsthalf
        else:
            return secondhalf


def exponentfunc(x, n):
    '''
    recursivly finds the exponent of the function depending on if it is even or odd
    :param x: one variable in the function
    :param n: another variable in the function
    :return: the result depending if it is even or odd
    '''
    if n <= 0:
        return 1

    else:
        y = n // 2
        m = exponentfunc(x, y)
        if (y%2  == 0):
            return m * m
        else:
            return m * m * x



def main():
    N = 100
    myList = [random.randint(-500, 500) for i in range(N)]

    x = int((random.randint(1,10)))
    n = int((random.randint(1,10)))
    print("The x value is: " , x)
    print("The n value is: " , n)

    print(myList)
    print("The sum of the numbers is: " + str(sum(myList)))
    print("The sum of the numbers using recSum1 is: " + str(recSum1(myList)))
    print("The sum of the numbers using recSum2 is: " + str(recSum2(myList)))
    print("The minimum value is the smaller minimums of the two halves is: " + str(minvalues(myList)))
    print("The recursive result for the xn problem is: " + str(exponentfunc(x,n)))

if __name__ == "__main__":
    main()