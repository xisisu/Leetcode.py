#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (44.71%)
# Total Accepted:    235.9K
# Total Submissions: 524.3K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[]]
        nxt = []
        for _ in range(numRows):
            cur = result[-1]
            for idx, val in enumerate(cur):
                if idx == 0:
                    nxt.append(1)
                else:
                    nxt.append(cur[idx-1] + val)
            nxt.append(1)
            result.append(nxt)
            nxt = []
        result.pop(0)
        return result
