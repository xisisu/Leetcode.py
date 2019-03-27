#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (49.39%)
# Total Accepted:    245.5K
# Total Submissions: 494.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in aschighing order, convert it to a
# height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, nums: List[int], low: int, high: int) -> TreeNode:
      if high < low or high >= len(nums) or low < 0:
        return None
      mid = (low + high) // 2
      root = TreeNode(nums[mid])
      root.left = self.helper(nums, low, mid-1)
      root.right = self.helper(nums, mid+1, high)
      return root

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
      return self.helper(nums, 0, len(nums)-1)

