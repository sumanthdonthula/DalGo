# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:12:48 2023

@author: Sumanth Donthula
"""

class sorting:
    
    def __init__(self, list):
        self.list = list
        self.count=0
        # Initialize the Sorting object with a list
    
    def selectionSort(self):
        """
        Perform selection sort on the list.
        """
        for i in range(len(self.list)-1):
            for j in range(i+1, len(self.list)):
                if self.list[i] > self.list[j]:
                    self.swap(i, j)
        # Time complexity: O(n^2), where n is the size of the list.
        # Selection sort compares and swaps elements, resulting in a quadratic time complexity.
    
    def bubbleSort(self):
        """
        Perform bubble sort on the list.
        """
        for i in range(len(self.list)):
            for j in range(len(self.list)-i-1):
                if self.list[j] > self.list[j+1]:
                    self.swap(j, j+1)
        # Time complexity: O(n^2), where n is the size of the list.
        # Bubble sort repeatedly compares and swaps adjacent elements, resulting in a quadratic time complexity.
    
    def insertionSort(self):
        """
        Perform insertion sort on the list.
        """
        for i in range(1, len(self.list)):
            for j in range(i, 0, -1):
                if self.list[j] < self.list[j-1]:
                    self.swap(j, j-1)
        # Time complexity: O(n^2), where n is the size of the list.
        # Insertion sort compares and shifts elements to their correct positions, resulting in a quadratic time complexity.
                    
    def swap(self, i, j):
        """
        Swap the elements at indices i and j in the list.
        """
        temp = self.list[i]
        self.list[i] = self.list[j]
        self.list[j] = temp
        
    

    def merge(self, sortedList1, sortedList2):
        sortedList = []
        i = 0
        j = 0

        if not sortedList1:
            return sortedList2

        if not sortedList2:
            return sortedList1

        while i < len(sortedList1) and j < len(sortedList2):
            if sortedList1[i] < sortedList2[j]:
                sortedList.append(sortedList1[i])
                i += 1
            else:
                sortedList.append(sortedList2[j])
                j += 1

        if i == len(sortedList1):
            sortedList.extend(sortedList2[j:])
        if j == len(sortedList2):
            sortedList.extend(sortedList1[i:])

        return sortedList
    # Time complexity: O(n), where n is the total number of elements in the two lists.
	# The merge operation takes linear time proportional to the combined size of the lists.
        
    def mergeSort(self):
        self.list = self.mergeSortRec(self.list)
    
    # Time complexity: O(n log n), where n is the size of the list.
	# Merge sort recursively divides the list into smaller halves and merges them in a sorted manner.
	# The time complexity is dominated by the divide-and-conquer process.

    def mergeSortRec(self, list):
        if len(list) <= 1:
            return list

        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        left = self.mergeSortRec(left)
        right = self.mergeSortRec(right)

        return self.merge(left, right)
    # Time complexity: O(n log n), where n is the size of the list.
	# The mergeSortRec method recursively divides the list into smaller halves and merges them in a sorted manner.
	# The time complexity is dominated by the divide-and-conquer process.
        
    def partition(self,start,end):
        self.count+=1
        init=start+1
        val=self.list[start]
        
        for cur in range(start+1,end):
            
            if self.list[cur]<val:
                if cur!=init:
                    self.swap(cur,init)
                init=init+1
        self.swap(start,init-1)

        return init-1
    
    def quickSort(self,start,end):


        if start<end:
            pivot=self.partition(start,end)
            self.quickSort(start,pivot)
            self.quickSort(pivot+1,end)
        


    


    
    
        
    def __str__(self):
        """
        Return a string representation of the list.
        """
        return f"{self.list}"
        # Time complexity: O(n), where n is the size of the list.
        # Converting the list to a string representation requires iterating over all elements.

        
        
sor=sorting([6,5,4,3,2,1])
sor.quickSort(0,len(sor.list))
print(sor.list)