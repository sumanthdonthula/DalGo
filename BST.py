# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:23:39 2023

@author: Sumanth Donthula
"""

# Define a class 'node' for a binary search tree (BST)
class node():
  
    def __init__(self, val=None):

        self.val = val
        self.left = None
        self.right = None

    # Method to add a node with a given value to the BST
    def addNode(self, val):

        if self.val is None:
            self.val = val

        elif val < self.val:
            if self.left is None:
                self.left = node(val)
            else:
                self.left.addNode(val)
        else:
            if self.right is None:
                self.right = node(val)
            else:
                self.right.addNode(val)

    # Method for in-order traversal and printing of BST nodes
    def inOrder(self):
        if self.left:
            if self.left.val:
                self.left.inOrder()
        if self:
            if self.val:
                print(str(self.val)+" ",end=" ")
        if self.right:
            if self.right.val:
                self.right.inOrder()
        
        return ""
        
    # Method for pre-order traversal and printing of BST nodes
    def preOrder(self):
        if self:
            if self.val:
                print(str(self.val)+" ",end=" ")

        if self.left:
            if self.left.val:
                self.left.preOrder()
        
        if self.right:
            if self.right.val:
                self.right.preOrder()
        
        return ""
    
    # Method for post-order traversal and printing of BST nodes
    def postOrder(self):
        if self.left:
            if self.left.val:
                self.left.postOrder()

        if self.right:
            if self.right.val:
                self.right.postOrder()

        if self:
            if self.val:
                print(str(self.val)+" ",end=" ")
        
        return ""
    
    # Method to find a value in the BST
    def find(self, val):

        if self.val == val:
            return True
        
        elif self is None:
            return False
        
        if self.val < val:
            if self.right:
                return self.right.find(val)
            else:
                return False
        
        elif self.val > val:
            if self.left:
                return self.left.find(val)
            else:
                return False
        
    # Method to find the minimum node in the BST
    def min(self):

        if self.left == None:
            return self
        else:
            return self.left.min()
        
    # Method to find the maximum node in the BST
    def max(self):

        if self.right == None:
            return self
        else:
            return self.right.max()
        
    # Method to find the minimum value in the BST
    def minVal(self):

        if self.left == None:
            return self.val
        else:
            return self.left.minVal()
        
    # Method to find the maximum value in the BST
    def maxVal(self):

        if self.right == None:
            return self.val
        else:
            return self.right.maxVal()
        
    # Method to delete a node with a given value from the BST
    def delNode(self, val):
            
        if self.val == val:
            if self.left:
                temp = self.left.max()
                self.val = temp.val
                temp.val = None
                temp.left = None
                temp.right = None
            
            elif self.right:
                temp = self.left.min()
                self.val = temp.val
                temp.val = None
                temp.left = None
                temp.right = None
            
            else:
                self.val = None
                self.left = None
                self.right = None

        elif self.val < val:
            self.right.delNode(val)

        else:
            self.left.delNode(val)
        
        return ""

# Create a root node for the Binary Search Tree (BST)
BST = node(5)

# Add nodes to the BST
BST.addNode(3)
BST.addNode(7)
BST.addNode(2)
BST.addNode(4)
BST.addNode(6)
BST.addNode(8)

# Print the BST using pre-order, post-order, and in-order traversals
print("Pre-order:")
print(BST.preOrder())
print("Post-order:")
print(BST.postOrder())
print("In-order:")
print(BST.inOrder())
