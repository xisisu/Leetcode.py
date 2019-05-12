#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     if root is None: return []
    #     result, cur = [], []
    #     cur.append(root)
    #     while len(cur) > 0:
    #         tmp, nxt = [], []
    #         for node in cur:
    #             tmp.append(node.val)
    #             for n in node.children:
    #                 nxt.append(n)
    #         cur = nxt
    #         result.append(tmp)
    #     return result

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        q, ret = [root], []
        while len(q) > 0:
            ret.append([n.val for n in q])
            q = [c for n in q for c in n.children if c]
        return ret
