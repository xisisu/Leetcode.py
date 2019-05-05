#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for d in [2,3,5]:
            while num % d == 0:
                num = num // d
        return num == 1
        
