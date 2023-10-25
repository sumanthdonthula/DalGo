# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:23:39 2023

@author: Sumanth Donthula
"""

class node:
  
    def __init__(self,val=None):
        self.val=val
        self.next=None


    def add(self,val):

        if self.val==None:
            self.val=val

        elif self.next==None:
            curNode=node(val)
            self.next=curNode
        else:
            self.next.add(val)
        
        return()
        
    def traverse(self):
        temp=self
        while temp!=None:
            print(temp.val)
            temp=temp.next
    
    def delete(self,val):

        if self.val==val:
            self.val=self.next.val
            if self.next.next!=None:
                self.next=self.next.next
            else:
                self.next=None  
            return
    
        while self!=None:
            
            if self.next!=None and self.next.val==val:
                self.next=self.next.next
                return

            self=self.next
    
    


ll=node(4)
ll.add(2)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(3)
ll.add(2)
ll.add(2)
ll.delete(4)
ll.delete(2)
ll.delete(2)
ll.traverse()