#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (33.06%)
# Total Accepted:    425.9K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
#
# Input: ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Note:
#
# All given inputs are in lowercase letters a-z.
#
#


class Solution:
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #   if not strs:
    #     return ""
    #   shortest = min(strs, key=len)
    #   for idx, c in enumerate(shortest):
    #     for s in strs:
    #       if s[idx] != c:
    #         return shortest[:idx]
    #   return shortest

    def longestCommonPrefix(self, strs: List[str]) -> str:
        for idx, letter_at_pos_i in enumerate(zip(*strs)):
            if len(set(letter_at_pos_i)) > 1:
                return strs[0][:idx]
        return min(strs) if strs else ""
