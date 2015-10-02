#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        length = len(nums)
        index = 0
        count = 0
        while count < length:
        	if(nums[index]==0):
        		nums.pop(index)
        		nums.append(0)
        		index -= 1       	
        	index += 1
        	count += 1


import unittest

class TestSolution(unittest.TestCase):

	def setUp(self):
		self.solution = Solution()

	def test1(self):
		indata = [0,1,2,3]
		self.solution.moveZeroes(indata)
		self.assertEqual(indata, [1,2,3,0])

	def test_all_zero(self):
		indata = [0,0,0,0]
		self.solution.moveZeroes(indata)
		self.assertEqual(indata, [0,0,0,0])


