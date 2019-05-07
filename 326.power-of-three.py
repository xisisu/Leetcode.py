#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n % 3 == 0 and n > 0:
            n = n // 3
        return n == 1
