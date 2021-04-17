# Author: Dani Rowe
# Date: October 20th, 2020
# Description: tests the three different types of traversals by looping
# through the tree

class BinaryTree:
    def __init__(self, payload = None, leftChild = None, rightChild = None):
        '''
        Constructor
        :param payload (any value): default None
        :param leftChild (a Binary Tree): default None
        :param rightChild (a Binary Tree): default None
        '''
        self.__payload = payload
        self.__leftChild = leftChild
        self.__rightChild = rightChild

    def getPayload(self):
        '''
        returns the current payload
        :return: the current payload
        '''
        return self.__payload

    def setPayload(self, payload):
        '''
        sets the current payload to the payload
        :param payload: sets the current payload to the payload
        :return: does not return anything
        '''
        self.__payload = payload

    def getLeftChild(self):
        '''
        returns the current LeftChild
        :return: the current LeftChild
        '''
        return self.__leftChild

    def setLeftChild(self, leftChild):
        '''
        sets the current leftChild to the leftChild
        :return: the current leftChild to the leftChild
        '''
        self.__leftChild = leftChild

    def getRightChild(self):
        '''
        returns the current RightChild
        :return: the current RightChild
        '''
        return self.__rightChild

    def setRightChild(self, rightChild):
        '''
        sets the current rightChild to the rightChild
        :return: the current rightChild to the rightChild
        '''
        self.__rightChild = rightChild

    def __str__(self):
        '''
        converts the tree to a string represenation do an in-order traversal
        :return: string
        '''
        return self.inorderTraversal()

    def inorderTraversal(self): # not done -- rearrange spaces correct?
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
            result += " " + str(self.getPayload())

            # visit the right subtree
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().inorderTraversal()

            return result

    def preorderTraversal(self):
        '''
        This function produces a preorder traversal of the tree.
        :return: a string that results from a preorder traversal
        '''
        result = ""
        if self.isEmpty():
            return result
        else:
            #visit the root node
            result += str(self.getPayload())

            #visit the left subtree
            if self.getLeftChild() is not None:
                result += " " + self.getLeftChild().preorderTraversal()

            #visit the right subtree
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().preorderTraversal()

            return result

    def postorderTraversal(self): # not done -- rearrange
        '''
        This function produces a preorder traversal of the tree.
        :return: a string that results from a preorder traversal
        '''
        result = ""
        if self.isEmpty():
            return result
        else:
            # visit the left subtree
            if self.getLeftChild() is not None:
                result += self.getLeftChild().postorderTraversal()

            # visit the right subtree
            if self.getRightChild() is not None:
                result += " " + self.getRightChild().postorderTraversal()

            # visit the root node
            result += " " + str(self.getPayload())

            return result


    def isEmpty(self):
        '''
        returns True if the tree is empty, False otherwise
        :return (boolean): True if the tree is empty, False otherwise
        '''
        # It is not really possible to call the isEmpty if you don't have
        # an object, so it really couldn't happen that self is None.
        return self is None or self.getPayload() is None

def main():
    BT = BinaryTree()
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)

    BT.setPayload(101)
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)

    BT.setLeftChild(BinaryTree(50))
    print(BT)

    BT.setRightChild(BinaryTree(250))
    print(BT)

    BT.getLeftChild().setLeftChild(BinaryTree(42))
    print(BT)

    BT.getLeftChild().getLeftChild().setLeftChild(BinaryTree(31))
    print(BT)

    BT.getRightChild().setRightChild(BinaryTree(315))
    print(BT)

    BT.getRightChild().setLeftChild(BinaryTree(200))
    print(BT)

    print("Inorder traversal: " + BT.inorderTraversal())
    print("Preorder traversal: " + BT.preorderTraversal())
    print("Postorder traversal: " + BT.postorderTraversal())

#creates the construct
if __name__  == "__main__":
    main()
