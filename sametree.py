#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        pq, qq=queue.Queue(),queue.Queue()
        pq.put(p)
        qq.put(q)

        while(!pq.empty()):
        	if(qq.empty()):
        		return False
        	pitem = pg.get()
        	qitem = qq.get()
        	pv = pitem.value
        	qv = qitem.value
        	if(pv != qv):
        		return False
        	if(pitem.left!=None):
        		if(qitem.left==None):
        			return False
        		pq.put(pitem.left)
        		qq.put(qitem.left)

        	if(pitem.right!=None):
        		if(qitem.right==None):
        			return False
        		pq.put(pitem.right)
        		qq.put(qitem.right)
        return True

