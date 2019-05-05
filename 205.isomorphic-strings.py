#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (36.78%)
# Total Accepted:    195.3K
# Total Submissions: 527.6K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#
#


class Solution:
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #     s_to_t = {}
    #     t_to_s = {}
    #     for idx, c in enumerate(s):
    #         if c in s_to_t and s_to_t[c] != t[idx]:
    #             return False
    #         s_to_t[c] = t[idx]
    #         if t[idx] in t_to_s and t_to_s[t[idx]] != c:
    #             return False
    #         t_to_s[t[idx]] = c
    #     return True

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     d1, d2 = {}, {}
    #     for i, val in enumerate(s):
    #         d1[val] = d1.get(val, []) + [i]
    #     for i, val in enumerate(t):
    #         d2[val] = d2.get(val, []) + [i]
    #     return sorted(d1.values()) == sorted(d2.values())

    def isIsomorphic(self, s: str, t: str) -> bool:
        # return [s.find(i) for i in s] == [t.find(i) for i in t]
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
