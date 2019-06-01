#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (62.30%)
# Likes:    546
# Dislikes: 71
# Total Accepted:    107.2K
# Total Submissions: 171.8K
# Testcase Example:  '5'
#
# Given a positive integer, output its complement number. The complement
# strategy is to flip the bits of its binary representation.
# 
# Note:
# 
# The given integer is guaranteed to fit within the range of a 32-bit signed
# integer.
# You could assume no leading zero bit in the integer’s binary
# representation.
# 
# 
# 
# Example 1:
# 
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
# 
# 
# 
# Example 2:
# 
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
# 
# 
#
class Solution:
    # def findComplement(self, num: int) -> int:
    #     reverse = ''.join(['0' if x == '1' else '1' for x in bin(num).lstrip('0').lstrip('b')])
    #     return int(reverse, 2)

    # just do a xor with 111 on all bits
    def findComplement(self, num: int) -> int:
        mask = 1 << (len(bin(num)) - 2) # bin(num) = '0bxxx'
        return (mask - 1) ^ num

