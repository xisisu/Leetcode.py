#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return bin(n).count('1') == 1 if n > 0 else False        

