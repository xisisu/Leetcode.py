#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = sum(v&1 for v in collections.Counter(s).values())
        # palindrome can have a signle char in the middle
        return len(s) - odds + (odds>0)


