# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:23:39 2023

@author: Sumanth Donthula
"""

class heap:
    
    def __init__(self, list):
        self.list = list
        # Initialize the Sorting object with a list
        
    def heapify(self,list,i):

        left=2*i+1
        right=2*i+2
        large=i
        
        if left<len(list) and right<len(list) and list[i]>list[right] and list[i]>list[left]:
            return list
        
        elif left<len(list) and right<len(list) and list[i]<list[right] and list[left]<list[right]:
            self.swap(list,i,right)
            large=right
            
        elif right>=len(list) and left<len(list) and list[i]< list[left]:
            self.swap(list,i,left)
            large=left

        elif right<len(list) and left<len(list) and list[right]< list[left] and list[i]<list[left]:
                self.swap(list,i,left)
                large=left

        if large!=i:
            self.heapify(list,large)  
        return list
       
    def swap(self,list,i,j):
        temp=list[i]
        list[i]=list[j]
        list[j]=temp
        
    def buildMaxHeap(self,list):
        if len(list)==1:
            return list
        else:
            for i in range((len(list)//2-1),-1,-1):
                list=self.heapify(list,i)
        return list
    
    def heapSort(self):
        list = self.list
        sorted=[None]*len(list)
        
        # Build a max heap in O(n) time
    
        list=self.buildMaxHeap(list)
        
        sorted[len(sorted)-1]=list[0]
        
        print(list)
        self.swap(list,0,len(list)-1)
        print(list)
        for i in range(len(list)-1,0,-1):
            list=list[:i]
            list=self.heapify(list,0)
            sorted[i-1]=list[0]
            self.swap(list,0,i-1)          

        return sorted

    def __str__(self):
        """
        Return a string representation of the list.
        """
        return f"{self.list}"
        # Time complexity: O(n), where n is the size of the list.
        # Converting the list to a string representation requires iterating over all elements.
 
heap=heap([5,6,1,2,3])
print(heap.heapSort())
