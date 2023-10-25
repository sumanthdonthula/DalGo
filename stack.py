# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:37:45 2023

@author: Sumanth Donthula
"""

class stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack
        self.size = 0  # Initialize the size of the stack to 0
        self.top = -1  # Initialize the top index of the stack to -1
    
    def push(self, data):
        self.stack.append(data)  # Add the data to the top of the stack
        self.size += 1  # Increase the size of the stack by 1
        self.top += 1  # Increment the top index by 1
        # Time complexity: O(1)
    
    def pop(self):
        if self.stack:  # Check if the stack is not empty
            self.stack.pop(self.top)  # Remove the element at the top of the stack
            self.size -= 1  # Decrease the size of the stack by 1
            self.top -= 1  # Decrement the top index by 1
        else:
            print("Can't remove an element, stack is empty")  # Print an error message if the stack is empty
        # Time complexity: O(1)
                
    def __str__(self):
        # Return a string representation of the stack
        return f"{self.stack}"
        # Time complexity: O(n), where n is the size of the stack. The string conversion requires iterating over all elements.



s=stack()
s.push(5)
s.push(9)
s.pop()
print(s)