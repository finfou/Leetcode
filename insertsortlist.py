#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
        	return head
        # init 
        newHead = head
        preNode = newHead
        curNode = head.next
        # Skip parts already in order
        while(curNode!=None and curNode.val >= preNode.val):
            preNode=curNode
            curNode=curNode.next
        nextNode = None
        preNode.next = None
        # iterate through nodes to insert
        while curNode!=None:
        	nextNode = curNode.next
        	# check if insert before head
        	if curNode.val < newHead.val:
        		curNode.next = newHead
        		newHead = curNode
        	else:
	        	preNode = newHead        	
	        	ite = newHead.next
	        	# Find insertion position
	        	while ite!=None and (ite.val < curNode.val):
	        		preNode = ite
	        		ite = preNode.next
	        	# Insert
	        	curNode.next = preNode.next
	        	preNode.next = curNode
        	curNode = nextNode
        return newHead