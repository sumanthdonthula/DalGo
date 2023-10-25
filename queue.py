# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 13:37:45 2023

@author: Sumanth Donthula
"""

class queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue
        self.size = 0  # Initialize the size of the queue to 0
        self.front = 0  # Initialize the front index of the queue to 0
        
    def enqueue(self, data):
        self.queue.append(data)  # Add the data to the end of the queue
        self.size += 1  # Increase the size of the queue by 1
        # Time complexity: O(1)
    
    def dequeue(self):
        if self.queue:  # Check if the queue is not empty
            self.queue.remove(self.queue[self.front])  # Remove the element at the front of the queue
            self.size -= 1  # Decrease the size of the queue by 1
        else:
            print("Can't remove an element, queue is empty")  # Print an error message if the queue is empty
        # Time complexity: O(n), where n is the size of the queue. The remove operation requires searching for the element.
                
    def __str__(self):
        # Return a string representation of the queue
        return f"{self.queue}"
        # Time complexity: O(n), where n is the size of the queue. The string conversion requires iterating over all elements.



s=queue()
s.enqueue(5)
s.enqueue(9)
s.enqueue(11)
s.dequeue()
print(s)