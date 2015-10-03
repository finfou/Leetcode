#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

class SolutionRecur(object):
    def __init__(self):
        self.charset={}
        self.length = 0
        for i in range(1,27):
            self.charset[str(i)]=i
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        self.length = len(s)
        if self.length <= 2:
            if self.canDecode(s):
                return self.length
            return 1
        else:
            num += self.numDecodings1(s, 1)
            if self.canDecode(s[0] + s[1]):
                num += self.numDecodings1(s, 2)
        return num
        
    def numDecodings1(self, s, start):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        if (self.length-start) == 2:
            if self.canDecode(s[start] + s[start+1]):
                return 2
            return 1
        elif (self.length-start) == 1:
            return 1
        else:
            num += self.numDecodings1(s, start+1)
            if self.canDecode(s[start]+s[start+1]):
                num += self.numDecodings1(s, start+2)
        return num
        
    def canDecode(self, str):
        if self.charset.get(str) == None:
            return False
        return True

class Solution(object):
    def __init__(self):
        self.charset={}
        self.length = 0
        for i in range(1,27):
            self.charset[str(i)]=i

    def canDecode(self, str):
        if self.charset.get(str) == None:
            return False
        return True

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        n1, n2, n3 = 1, 1, 0
        if length == 0:
            return 0
        if s[0] == '0':
            return 0
        if length == 1:
            return 1
        if s[1] == '0':
            n2 = 0
            if self.canDecode(s[0]+s[1]):
                n2 = 1
        elif self.canDecode(s[0] + s[1]):
            n2 = 2
        
        if length == 2:
            return n2
        else:
            for i in range(2,length):
                if s[i]=='0':
                    if (s[i-1]!='1' and s[i-1]!='2'):
                        return 0 # invalid
                    else:
                        n3 = n1
                elif self.canDecode(s[i-1] + s[i]):
                    n3 = n1 + n2
                else:
                    n3 = n2
                n1 = n2
                n2 = n3
        return n3

import unittest

class TestSolution(unittest.TestCase):
    def testa(self):
        strA = "110"
        self.assertEqual(5, Solution().numDecodings(strA))