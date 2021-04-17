# Author: Danielle Rowe
# Date: October 27th, 2020
# Description: Creates a Binary Tree that we search through in order to find the
# minimum and maxiumum value, and figure out the position of the children using the height

#import the Binary Tree class from Binary Tree
from Lab8 import BinaryTree

#create a new class for the Binary Search Tree
class BinarySearchTree (BinaryTree):
    def __init__ (self, payload = None, leftChild = None, rightChild = None):
        '''
        Constructor
        :param payload (any comparable value) : the contents of the root
        :param leftChild (BinarySearchTree) : the left subtree
        :param rightChild (BinarySearchTree) : the right subtree
        '''
        BinaryTree.__init__(self, payload, leftChild, rightChild)
        if (self.getPayload() is None):
            # the height of an empty tree is -1
            self.__height = -1
        else:
            # The height of a leaf is 0
            # we can't use computeHeight here because we end up
            # callling it multiple times where there will be
            # new tree being created with "None" as the height.
            self.__height = 0

    def getHeight(self): # not done
        '''
        Returns the current height
        :return: the height
        '''
        return self.__height

    def computeHeight(self):
        '''
        Compute and set the height based upon the subtrees.
        The height is -1 for an empty tree, 0 for a leaf,
        or max if the heights of its children plus one.
        :return: None
        '''
        # The height of an empty tree is -1
        # The heigh of a leaf if 0
        height = -1

        if (self.getLeftChild() is not None):
            height = max(height, self.getLeftChild().getHeight())

        if (self.getRightChild() is not None):
            height = max(height, self.getRightChild().getHeight())

        # Assertion: the height at this point will be bigger of the heights
        # of the two subtrees. If this is a leaf, then the height will still
        # be a -1.
        self.__height = height +1

    # Disallow the setHeight(). We don't want the user to mess with the height.
    # We provide a computeHeight so that we can recompute it correctly.

    def setPayload(self, payload):
        '''
        Setter for the payload.
        :param payload (any comparable value): the contents of the root
        :return:None
        We need to overload the setPayload() from the BinaryTree.setPayload()
        because we have added the height.
        '''
        BinaryTree.setPayload(self, payload)
        self.computeHeight()

    def insert(self, x):
        '''
        Insert a new value into the BST.
        :param x (any comparable value): the contents of the root
        :return: None
        '''

        #Since self can't be a non-existent tree, the only way for it to be
        # an empty tree is if it has no payload
        if self.isEmpty():
            self.setPayload(x)

        #If this is a "<"  instead of a "<=", then duplicates will go in the
        # right subtree, preserving the order in which they were inserted
        elif x < self.getPayload():
            if self.getLeftChild() is None:
                #There is no left subtree
                self.setLeftChild(BinarySearchTree(x))
                self.computeHeight()
            else:
                # Recursively put into left subtree
                self.getLeftChild().insert(x)
                self.computeHeight()
        else: # x >= self.payload
            if self.getRightChild() is None:
                # There is no right subtree
                self.setRightChild(BinarySearchTree(x))
                self.computeHeight()
            else:
                # Recursively put into right subtree
                self.getRightChild().insert(x)
                self.computeHeight()

    def find(self, x):
        '''
        Find a value in the VST
        :param x (any comparable value): the contents of the root
        :return: The value in the tree that matches, or None if it is not there
        '''
        if self.isEmpty():
            return None
        elif x == self.getPayload():
            return self.getPayload()
        elif x < self.getPayload():
            if self.getLeftChild() is None:
                return None
            else:
                return self.getLeftChild().find(x)
        else:
            if self.getRightChild() is None:
                return None
            else:
                return self.getRightChild().find(x)

    def minValue(self): # not done - recursive
        '''
        Returns the minimum value in the tree
        :return: the minimum value in the tree
        '''
        # checks to see if the binary tree is empty
        if self.isEmpty():
            return None
        #if there are no more values on the left side of the binary tree return the payload
        elif self.getLeftChild() is None:
            return self.getPayload()
        #else if there is still leftChildren recursively find the last one
        else:
            return self.getLeftChild().minValue()

    def maxValue(self):
        '''
        Returns the maximum value of the tree
        :return: the maximum value of the tree
        '''
        #checks to see if the binary tree is empty
        if self.isEmpty():
            return None
        # if there are no more values on the right side of the binary tree return the payload
        elif self.getRightChild() is None:
            value =  self.getPayload()
        # else if there is still rightChildren recursively find the last one
        else:
            value =  self.getRightChild().maxValue()

        return value


    #def isBST(self):

    def inorderTraversal(self): # copy code from inorder traversal binary tree
        '''
        This function produces a inorder traversal of the tree.
        :return: a string that results from a inorder traversal
        '''
        result = ""
        if self.isEmpty():
            return result
        else:
            # visit the left subtree
            if self.getLeftChild() is not None:
                result += self.getLeftChild().inorderTraversal()

            # visit the root node
            result += " " + str(self.getPayload()) + "(" + str(self.getHeight()) + ")"

            # visit the right subtree
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().inorderTraversal()

            return result

    def isEmpty(self):
        '''
        checks if the function is empty
        :return:
        '''
        return self is None or self.getPayload() is None

def main():
    BST = BinarySearchTree()
    print("isEmpty() = " + str(BST.isEmpty()))
    print(BST)

    BST.insert(100)
    print(BST)
    BST.insert(190)
    print(BST)
    BST.insert(50)
    print(BST)
    BST.insert(90)
    print(BST)
    BST.insert(30)
    print(BST)
    BST.insert(40)
    print(BST)
    print("The height of the Binary Tree is: " , BST.getHeight())
    print("The min value of the Binary Tree is: ", BST.minValue())
    print("The max value of the Binary Tree is: ", BST.maxValue())

    print("Inorder traversal: " + BST.inorderTraversal())

#creates the construct
if __name__  == "__main__":
    main()







