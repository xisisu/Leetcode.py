#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (42.80%)
# Total Accepted:    372.2K
# Total Submissions: 866.9K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# But the following [1,2,2,null,3,null,3]  is not:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Note:
# Bonus points if you could solve it both recursively and iteratively.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isSymmetricTree(self, r1: TreeNode, r2: TreeNode) -> bool:
    #   if r1 and r2:
    #     return r1.val == r2.val and self.isSymmetricTree(r1.left, r2.right) and self.isSymmetricTree(r1.right, r2.left)
    #   return r1 is r2

    # def isSymmetric(self, root: TreeNode) -> bool:
    #   return not root or self.isSymmetricTree(root.left, root.right)        

    def isSymmetric(self, root: TreeNode) -> bool:
      if not root:
        return True
      cache = [[root.left, root.right]]
      while len(cache) > 0:
        left, right = cache.pop(0)  
        if left and right:
          if left.val != right.val:
            return False
          cache.append([left.left, right.right])
          cache.append([left.right, right.left])
        elif left is not right:
          return False
      return True
