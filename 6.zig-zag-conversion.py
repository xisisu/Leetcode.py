#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (31.50%)
# Likes:    1033
# Dislikes: 3223
# Total Accepted:    320.3K
# Total Submissions: 1M
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:
    #         return s
    #     res = [[] for _ in range(numRows)]
    #     idx, downward = 0, True
    #     for ch in s:
    #         res[idx].append(ch)
    #         if downward:
    #             idx += 1
    #             if idx == numRows:
    #                 idx -= 2
    #                 downward = False
    #         else:
    #             idx -= 1
    #             if idx < 0:
    #                 idx = 1
    #                 downward = True
    #     return ''.join([''.join(l) for l in res])

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        res = [''] * numRows
        idx, step = 0, 1
        for ch in s:
            res[idx] += ch
            if idx == numRows - 1:
                step = -1
            elif idx == 0:
                step = 1
            idx += step
        return ''.join(res)



