#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

class Solution(object):
    def __init__(self):
        self.charset={}
        for i in range(1,27):
            self.charset[str(i)]=i
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        if len(s) <= 2:
            if self.canDecode(s):
                return len(s)
            return 1
        else:
            num += self.numDecodings(s[1:])
            if self.canDecode(s[0:2]):
                num += self.numDecodings(s[2:])
        return num
        
    def canDecode(self, str):
        if str in self.charset.keys():
            return True
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testa(self):
        strA = "12"
        self.assertEqual(2, Solution().numDecodings(strA))