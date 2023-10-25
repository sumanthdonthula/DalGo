# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 12:42:20 2023

@author: Sumanth Donthula
"""

class unionFind:
    def __init__(self, list):
        self.list = list
        self.dict = {}  # Initialize an empty dictionary
        
        for i in range(len(list)):
            # Add a key-value pair to the dictionary, where the key is the current element from the list
            # and the value is a list containing the index i
            self.dict[list[i]] = [i]
        # Time complexity: O(n), where n is the length of the list
    
    def find(self, cityA, cityB):
        # Check if the values of cityA and cityB in the dictionary are the same
        if self.dict[cityA] == self.dict[cityB]:
            return "Connection Exists"
        else:
            return "No Connection Exists"
        # Time complexity: O(1)
    
    def union(self, cityA, cityB):
        # Update the index values of cityA with the values of cityB in the dictionary
        self.dict[cityA] = self.dict[cityB]
        # Time complexity: O(1)
      
    def __str__(self):
        # Return a string representation of the dictionary
        return f"{self.dict}"
        # Time complexity: O(1)


    
    
        
    
v1=unionFind(["Ongole","Guntur","Nellore"])
v1.union("Ongole","Guntur")
print(v1)
v1.union("Nellore","Ongole")
print(v1.find("Ongole","Nellore"))
print(v1)