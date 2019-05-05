#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    #     if not root:
    #         return []
    #     if not root.left and not root.right:
    #         return [str(root.val)]
    #     result = []
    #     for path in self.binaryTreePaths(root.left):
    #         result.append(str(root.val)+'->'+path)
    #     for path in self.binaryTreePaths(root.right):
    #         result.append(str(root.val)+'->'+path)
    #     return result

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result, stack = [], [(root, "")]
        while stack:
            node, path = stack.pop()
            cur = path + str(node.val)
            if not node.left and not node.right:
                result.append(cur)
            if node.right:
                stack.append((node.right, cur+'->'))
            if node.left:
                stack.append((node.left, cur+'->'))
        return result
