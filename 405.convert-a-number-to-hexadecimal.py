#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#
class Solution:
    def toHex(self, num: int) -> str:
        chars = '0123456789abcdef'
        res = ''
        for _ in range(8): # 8 bit in total, handels the negative num prob.
            res = chars[num & 15] + res # handles the num=0 prob.
            num >>= 4
            if num == 0:
                break
        return res

