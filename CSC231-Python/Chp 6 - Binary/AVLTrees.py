#Author: Danielle Rowe
#Date: November 3rd, 2020
#Description: Insert values into an AVL Tree, and check to
# make sure the AVL Tree is balanced on both sides.

from BinarySearchTree import BinaryTree
from BinarySearchTree import BinarySearchTree

class AVLTree(BinarySearchTree):

    def balanced(self):
        '''
        Returns True if the tree is unbalanced
        :return (boolean): Returns True if tree is unbalanced, false otherwise
        '''
        if self.getLeftChild is not None:
            lHeight = self.getLeftChild().getHeight()
        else:
            lHeight = -1
        if self.getRightChild() is not None:
            rHeight = self.getRightChild().getHeight()
        else:
            rHeight = -1

        return (abs(lHeight - rHeight) < 2)

    def balanced(self):
        '''
        Returns True if the tree is unbalanced
        :return (boolean): Returns True if tree is unbalanced, False otherwise
        '''
        if self.getLeftChild() is not None:
            lHeight = self.getLeftChild().getHeight()
        else:
            lHeight = -1

        if self.getRightChild() is not None:
            rHeight = self.getRightChild().getHeight()
        else:
            rHeight = -1

        return abs(lHeight - rHeight < 2)

    def insert(self, x):
        '''
        Insert a new value into the AVL Tree.
        :param x (any comparable value): the contents of the root
        :return: the new root of the tree
        '''

        if self.isEmpty():
            self.setPayload(x)
            return self

        elif x < self.getPayload():
            if self.getLeftChild() is None:
                self.setLeftChild(AVLTree(x))
                self.computeHeight()
                return self
            else:
                self.setLeftChild(self.getLeftChild().insert(x))
                if not self.balanced():
                    #Case 1:
                    if x < self.getLeftChild().getPayload():
                        return self.rotateWithLeftChild()
                    #Case 2:
                    else:
                        self.setLeftChild(self.getLeftChild().rotateWithRightChild())
                        return(self.rotateWithLeftChild())

                self.computeHeight()
                return self
        else:
            if self.getRightChild() is None:
                self.setRightChild(AVLTree(x))
                self.computeHeight()
                return self
            else:
                self.setRightChild(self.getRightChild().insert(x))
                if not self.balanced():
                    # Case 4:
                    if x >= self.getRightChild().getPayload():
                        return self.rotateWithRightChild()
                    # Case 3:
                    self.setRightChild(self.getRightChild().rotateWithLeftChild())
                    return (self.rotateWithRightChild())
                self.computeHeight()
                return self

    def rotateWithLeftChild(self):
        '''
        Rotate self with its left child
        :return: the new root of the tree
        '''

        k1 = self.getLeftChild()

        #Move the child of k1 over to self
        self.setLeftChild(k1.getRightChild())

        #Hang self off of k1
        k1.setRightChild(self)

        #Recompute the heights of both
        self.computeHeight()
        k1.computeHeight()

        #return the new root
        return k1

    def rotateWithRightChild(self):
        '''
        Rotate self with its right child
        :return: the new root of the tree
        '''

        k2 = self.getRightChild()

        #Move the child k2 over to self
        self.setRightChild(k2.getLeftChild())

        #Hang self off of k1
        k2.setLeftChild(self)

        #recompute the heights of both
        self.computeHeight()
        k2.computeHeight()

        #return the new root
        return k2

def main():

    avlBST = AVLTree()
    print(avlBST)
    x = 0

    values = [63, 41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]

    # for i in range(len(values)):
    #     avlBST = avlBST.insert(values[i])

    for x in values:
        avlBST = avlBST.insert(x)
        #print(avlBST)

#creates the construct
if __name__  == "__main__":
    main()
