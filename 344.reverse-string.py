#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
class Solution:
    # def reverseString(self, s: List[str]) -> None:
    #     """
    #     Do not return anything, modify s in-place instead.
    #     """
    #     l, h = 0, len(s)-1
    #     while l < h:
    #         s[l], s[h] = s[h], s[l]
    #         l += 1
    #         h -= 1

    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

