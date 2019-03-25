#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (39.64%)
# Total Accepted:    265.8K
# Total Submissions: 668K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution:
    def countAndSay(self, n: int) -> str:
      if n < 1:
        return ""

      s = "1"
      for _ in range(n-1):
        cur, count, res = s[0], 0, ""
        for val in s:
          if val != cur:
            res += str(count)
            res += str(cur)
            cur, count = val, 1
          else:
            count += 1
        res += str(count)
        res += str(cur)
        s = res
      return s

