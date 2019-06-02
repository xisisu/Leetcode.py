#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.10%)
# Likes:    3617
# Dislikes: 351
# Total Accepted:    560.2K
# Total Submissions: 2.1M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     def helper(s: str, left: int, right: int) -> int:
    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             left -= 1
    #             right += 1
    #         return s[left+1:right]
    #     res = ""
    #     for i in range(len(s)):
    #         s1 = helper(s, i, i)
    #         s2 = helper(s, i, i+1)
    #         if len(s1) > len(res):
    #             res = s1
    #         if len(s2) > len(res):
    #             res = s2
    #     return res

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        dp = [[False] * n for _ in range(n)]
        for length in range(n):
            for start in range(n-length):
                end = start + length
                if s[start] != s[end]:
                    continue
                if abs(start-end) <= 1:
                    dp[start][end] = True
                else:
                    dp[start][end] = dp[start+1][end-1]
                if dp[start][end]:
                    res = s[start:end+1]
        return res
        
