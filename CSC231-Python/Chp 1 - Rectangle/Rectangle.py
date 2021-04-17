#author : Dani Rowe
#date : sept 1st 2020
#description : this program creates a class for a rectangle. it provides getters and setters
#for class variables, a draw function, an erase (or undraw) function, and an area function.

class Rectangle:
    def __int__(self, x = 0, y = 0, width = 10, height = 10, \
                linecolor = "black", fillcolor = "white"):

        '''
        Constructor:
        :param x (int): x coordinate of the upper left hand corner
        :param y (int): y coordinate of the upper left hand corner
        :param width (int): width (in pixels)
        :param height (int) : width (in pixels)
        :param linecolor (string): width (in pixels)
        :param fillcolor (string): width (in pixels)
        '''

        self.__x = x
        self.__y = y
        if width < 0:
            self.__width = 0
        if height < 0:
            self.__height = 0
        else:
            self.__height = height

        self.__linecolor = linecolor
        self.__fillcolor = fillcolor

        def setX(self, x):
            self.__x = x

        def getY(self):
            return self.__Y

        def setY(self, y):
            self.__y = y

        def getwidth(self):
            return self.__width

        def setwidth(self, width):
            self.__width = width

        def getheight(self):
            return self.__height

        def setheight(self, height):
            self.__height = height

        def getlinecolor(self):
            return self.__linecolor

        def setlinecolor(self, color):
            self.__linecolor = color

        def getfillcolor(self):
            return self.__fillcolor

        def setfillcolor(self, color):
            self.__fillcolor = color


        #go to code in video from Lab1 rectangle if want the rest





