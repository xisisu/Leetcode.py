#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# https://leetcode.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (42.21%)
# Total Accepted:    190.9K
# Total Submissions: 449K
# Testcase Example:  '3'
#
# Given a non-negative index k where k ≤ 33, return the k^th index row of the
# Pascal's triangle.
#
# Note that the row index starts from 0.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 3
# Output: [1,3,3,1]
#
#
# Follow up:
#
# Could you optimize your algorithm to use only O(k) extra space?
#
#


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        nxt = []
        for _ in range(rowIndex+1):
            cur = nxt
            nxt = []
            for idx, val in enumerate(cur):
                if idx == 0:
                    nxt.append(1)
                else:
                    nxt.append(cur[idx-1] + val)
            nxt.append(1)
        return nxt
