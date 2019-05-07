#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
