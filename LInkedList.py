# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:36:56 2022

@author: joeeb
"""
from random import randint            
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else :
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index +=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                
    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1
            node = node.next
        return result
    
    def generate(self, n, min_value, max_value, location):
        self.head = None
        self.tail = None
        for i in range(n):
            self.insertSLL(randint(min_value, max_value), location)
        return self
    
customLL = SLinkedList()
customLL.generate(10, 0, 99, 0)
print([node.value for node in customLL])   
print(len(customLL))   
            