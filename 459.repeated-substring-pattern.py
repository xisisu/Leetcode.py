#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (39.73%)
# Likes:    775
# Dislikes: 95
# Total Accepted:    79.4K
# Total Submissions: 199.2K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: False
# 
# 
# Example 3:
# 
# 
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#
class Solution:
    # def repeatedSubstringPattern(self, s: str) -> bool:
    #     for i in range(1, len(s) // 2):
    #         if len(s) % i != 0:
    #             continue
    #         sub = s[:i]
    #         repeat = len(s) // i
    #         if s == sub*repeat:
    #             return True
    #     return False

    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s*2)[1:-1]
