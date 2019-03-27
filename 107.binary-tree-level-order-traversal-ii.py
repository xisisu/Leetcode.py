#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (45.76%)
# Total Accepted:    214.2K
# Total Submissions: 466.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result, queue = [], []
        cur, nxt = [], []
        if root:
            cur.append(root)
        while len(cur) > 0:
            tmp = cur.pop(0)
            queue.append(tmp.val)
            if tmp.left:
                nxt.append(tmp.left)
            if tmp.right:
                nxt.append(tmp.right)
            if len(cur) == 0:
                cur, nxt = nxt, cur
                result.append(queue)
                queue = []
        return result[::-1]
