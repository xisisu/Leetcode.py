#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.48%)
# Total Accepted:    373.1K
# Total Submissions: 919.8K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
      l, h = 0, len(nums)-1
      while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
          return mid
        elif nums[mid] < target:
          l = mid+1
        else: # nums[mid] > target
          h = mid-1
      return l

