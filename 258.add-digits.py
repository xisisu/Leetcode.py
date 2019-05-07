#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#


class Solution:
    # def addDigits(self, num: int) -> int:
    #     if num < 10:
    #         return num
    #     else:
    #         return self.addDigits(num//10 + num%10)

    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum([int(i) for i in str(num)])
        return num
