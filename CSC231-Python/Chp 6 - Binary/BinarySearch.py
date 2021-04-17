'''
Author: Dani Rowe
Date: October 13th, 2020
Description: Preforms a Binary Search
'''

import random

def BinarySearch(sortList, x):
    '''
    Recursivly preforms a binary search on a list, and deletes the values
    from the list as it goes on. Splits the list into two halves.
    :param sortList: the sorted list
    :param x: the value we are comparing
    :return: None or the midpoint
    '''
    if len(sortList) <= 0:
        return None
    elif len(sortList) == 1:
        if x == sortList[0]:
            return sortList[0]
        else:
            return None

    else:
        midpoint = len(sortList) // 2
        if x == sortList[midpoint]:
            return sortList[midpoint]
        elif x < sortList[midpoint]:
            return BinarySearch(sortList[:midpoint-1], x)
        else:
            return BinarySearch(sortList[midpoint - 1:], x)

def main():
    N = 100
    myList = [random.randint(-50, 50) for i in range(N)]

    myList.sort()
    print(myList)

    for i in range(N):
        value = random.randint(-50,50)
        found = BinarySearch(myList, value)
        if found is None:
            print("Value" + str(value) + "not found")
        else:
            print("Found Value" + str(found))
if __name__ == "__main__":
    main()