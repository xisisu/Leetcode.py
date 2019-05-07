#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#


class Solution:
    # def isPowerOfFour(self, num: int) -> bool:
    #     while num % 4 == 0 and num > 0:
    #         num = num // 4
    #     return num == 1

    def isPowerOfFour(self, num: int) -> bool:
        s = str(bin(num))
        return num > 0 and s.count('1') == 1 and s.count('0') % 2 == 1
