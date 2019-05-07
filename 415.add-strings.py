#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
class Solution:
    def get_val(self, num: str, idx: int) -> int:
        return 0 if idx >= len(num) else int(num[idx])

    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        res, carry = '', 0
        for i in range(max(len(num1), len(num2))):
            cur = carry + self.get_val(num1, i) + self.get_val(num2, i)
            res = str(cur % 10) + res
            carry = cur // 10
        return str(carry)*(carry>0) + res

