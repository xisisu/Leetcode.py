#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (30.32%)
# Total Accepted:    332.5K
# Total Submissions: 1.1M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:


    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s)-1
        s = s.lower()
        while low < high:
            while not s[low].isalnum() and low < high:
                low += 1
            while not s[high].isalnum() and low < high:
                high -= 1
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

