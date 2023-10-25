# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:23:39 2023
@author: Sumanth Donthula
"""

# Define a class 'node' for a doubly linked list node
class node:
  
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

    # Method to add a new node with a given value to the end of the doubly linked list
    def add(self, val):

        if self.val is None:
            self.val = val
            self.prev = None

        elif self.next is None:
            curNode = node(val)
            self.next = curNode
            curNode.prev = self

        else:
            # Recursively call 'add' on the next node to add the value
            self.next.add(val)

    # Method to traverse and print the values of the doubly linked list
    def traverse(self):
        temp = self
        while temp is not None:
            if temp.val:
                print(temp.val, end=" ")
            temp = temp.next
        return ""

    # Method to traverse and print the values of the doubly linked list in reverse order
    def reverseTraverse(self):

        temp = self
        while temp.next is not None:
            temp = temp.next

        tail = temp
        print(tail.prev.val)  # Print the value of the previous node of the tail
        while tail is not None:
            if tail.val:
                print(tail.val, end=" ")
            tail = tail.prev  # Move backward through the list
        return ""

    # Method to delete a node with a given value from the doubly linked list
    def delete(self, val):

        if self.val == val:
            self.val = self.next.val
            if self.next.next is not None:
                self.next = self.next.next
                self.next.prev = self
            else:
                self.next = None  

        while self is not None:
            
            if self.next is not None and self.next.val == val:

                self.next = self.next.next

                if self.next is not None:
                    self.next.prev = self

                return

            self = self.next

# Create a doubly linked list with an initial value of 4
ll = node(4)

# Add values to the doubly linked list
ll.add(2)
ll.add(3)
ll.add(5)

# Delete nodes with a specific value from the doubly linked list
ll.delete(4)

# Print the doubly linked list in reverse order
print(ll.reverseTraverse())
