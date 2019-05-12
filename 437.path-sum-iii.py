#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def helper(self, root: TreeNode, sum: int) -> int:
    #     if root is None:
    #         return 0
    #     return int(root.val == sum) + self.helper(root.left, sum-root.val) + self.helper(root.right, sum-root.val)
        

    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     if root is None:
    #         return 0
    #     return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, root, sum, so_far, cache):
        if root is None:
            return
        key = so_far + root.val
        complement = key - sum
        if complement in cache:
            self.result += cache[complement]
        
        cache.setdefault(key, 0)
        cache[key] += 1
        self.helper(root.left, sum, key, cache)
        self.helper(root.right, sum, key, cache)
        cache[key] -= 1 # This is very important, as it ensures it does not mass with follow up cases.

    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result


