'''
Author: Danielle M. Rowe
Date: September 1st, 2020
Description: Create a class Fraction then create several functions that take solve the
    fraction in different ways (addition, subtraction, turning it into a string, etc), and
    print the output at the end
'''



class Fraction:
    def __init__(self, num = 0, den = 1):
        '''
        Constructor
        :param num (integar): Numerator: default 0
        :param den (integar): Denominator: default 1
        '''

        g = self.__gcd(num,den)
        self.__num = num // g
        self.__den = den // g
        if (self.__den < 0):
            self.__num = -self.__num
            self.__den = -self.__den

    def __str__(self):
        '''
        Returns a string representation of the fraction
        :param: None
        :return: returns the string representation of the fraction
        '''
        return (str(self.__num) + "/" + str(self.__den))

    def __add__(self, other):
        '''
        Returns a new fraction that is the addition of self and other
        :param other: (fraction)
        :return: fraction that is the addition of self and other
        '''
        mul1 = self.__num * other.__den
        mul2 = self.__den * other.__num
        return self.__class__(mul1 + mul2,mul2)

    def __sub__(self, other):
        '''
            Returns a new fraction that is the subtraction of self and other
            :param other: (fraction)
            :return: fraction that is the subtraction of self and other
        '''
        mul1 = self.__num * other.__den
        mul2 = self.__den * other.__num
        return self.__class__(mul1 - mul2, mul2)

    def __mul__(self, other):

        '''
            Returns a new fraction that is the multiplication of self and other
            :param other: (fraction)
            :return: fraction that is the multiplication of self and other
        '''
        mul1 = self.__num * other.__den
        mul2 = self.__den * other.__num
        return self.__class__(mul1 * mul2, mul2)


    def __truediv__(self, other):
        '''
        Returns a new fraction that is the division of the current
            fraction and the parameter

        :param other: (fraction)
        :return: returns self divided by other

        a/b / c/d = * a/b * d/c = ab/bc
        '''

        num = self.__num * other.__den
        den = self.__den * other.__num
        return self.__class__(num, den)



    def __gcd(self,m,n):
        '''
            Returns the greatest common demoninator between two integers
            :param: m and n
            :return: the greatest common demoninator
        '''
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn

        return n








def main():
    f1 = Fraction(10,16)
    f2 = Fraction(-4,-3)
    f3 = Fraction(3,-4)

    print("f1 =", f1)
    print("f2 =", f2)
    print("f3 =", f3)

    print(f1, "plus", f2, "=", f1 + f2)
    print(f1, "plus", f3, "=", f1 + f3)
    print()

    print(f1, "minus", f2, "=", f1-f2)
    print(f1, "minus", f3, "=", f1-f3)
    print()

    print(f1, "times", f2, "=", f1*f2)
    print(f1, "times", f3, "=", f1*f3)
    print()

    print(f1, "divided by", f2, "=", f1/f2)
    print(f1, "divided by", f3, "=", f1/f3)
    print()



if __name__ == "__main__":
    main()