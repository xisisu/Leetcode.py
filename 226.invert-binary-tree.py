#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if not root or (not root.left and not root.right):
    #         return root
    #     else:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #         return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        q = []
        q.append(root)
        while len(q) > 0:
            cur = q.pop(0)
            cur.left, cur.right = cur.right, cur.left
            if cur.left != None:
                q.append(cur.left)
            if cur.right != None:
                q.append(cur.right)
        return root

