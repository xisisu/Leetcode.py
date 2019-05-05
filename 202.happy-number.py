#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (44.37%)
# Total Accepted:    222.8K
# Total Submissions: 498.4K
# Te n777777
# /9******************************1`1se Example:  '19'
#
# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
#
# Example: 
#
#
# Input: 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#


class Solution:
    # def helper(self, n: int) -> int:
    #     result = 0
    #     while n > 0:
    #         cur = n % 10
    #         n //= 10
    #         result += cur * cur
    #     return result
    # def isHappy(self, n: int) -> bool:
    #     seen_num = set()
    #     while n != 1:
    #         if n in seen_num:
    #             return False
    #         seen_num.add(n)
    #         n = self.helper(n)
    #     return True

    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum([int(i)**2 for i in str(n)])
        return True
