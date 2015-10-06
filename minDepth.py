#!/usr/bin/env python
#! -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	
	def isLeaf(sef, node):
		if node.left == None and node.right == None:
			return True;
		return False;

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 1
        import Queue
        q = Queue.Queue()
        q.put({'node':root,'level':level})

        while(not q.empty()):
        	item = q.get();
        	if self.isLeaf(item['node']):
        		return item['level']
        	if item['node'].left != None:
        		q.put({'node':item['node'].left, 'level':item['level']+1})
        	if item['node'].right != None:
        		q.put({'node':item['node'].right, 'level':item['level']+1})





