#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.26%)
# Likes:    5563
# Dislikes: 310
# Total Accepted:    934.9K
# Total Submissions: 3.3M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     chars, res = set(), 0
    #     start, end = 0, 0
    #     while end < len(s):
    #         if s[end] not in chars:
    #             chars.add(s[end])
    #         else:
    #             res = max(res, len(chars))
    #             while s[start] != s[end]:
    #                 chars.remove(s[start])
    #                 start += 1
    #             start += 1
    #         end += 1
    #     return max(res, len(chars))
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        map, res, start = {}, 0, 0
        for k, v in enumerate(list(s)):
            if v in map and start <= map[v]:
                start = map[v]+1
            else:
                res = max(res, k-start+1)
            map[v] = k
        return res
