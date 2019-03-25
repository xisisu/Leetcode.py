#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.07%)
# Total Accepted:    283.8K
# Total Submissions: 741.6K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def valAtPos(self, a: str, pos: int) -> int:
      return 0 if pos >= len(a) else int(a[pos])

    def addBinary(self, a: str, b: str) -> str:
      res, a, b, carry = "", a[::-1], b[::-1], 0
      for idx in range(max(len(a), len(b))):
        val = carry + self.valAtPos(a, idx) + self.valAtPos(b, idx)
        res += str(val % 2)
        carry = val // 2
      if carry:
        res += str(carry)
      return res[::-1]
