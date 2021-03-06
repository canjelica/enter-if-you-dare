Write code to do an inorder BST traversal with recursion  and without recursion. Explain in which case you would choose one implementation over the other. Explain the runtime of each.
AnswerAdd Tags

linked list problem

1. Pascals Triangle 2. Minimum Squares sum up to a number

Questions on coding, machine learning and statistics  

ASP.NET 

Write a javascript class that subscript msg from server and print it, or send msg to the server.  

Asked to design a kind of data structure that is suitable for frequent adding and deleting event at the head, write add, delete, getLength function, and initialize it in the main function, try to debug if there is an exception.  

he first round was about binary tree serialization and deserialization, but there was some extra requirements. The second and the third rounds were about linked lists. These three rounds of algorithm and data structures were not hard. Unfortunately, the fourth round was bunch of questions about operating systems and networks. These questions were really difficult and full of details.

How sliding window in TCP can increase the network efficiency?  

skyline problem
Find the greatest divisor of a number  

Given two strings, find the longest common Substring  

 resume experience in depth. Asked me to explain my project in depth. Questions were from leetcode medium level. There were 4 rounds. 2 of them were coding and one was project design explanation. Over a good experience

 

 #!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

if __name__ == '__main__':