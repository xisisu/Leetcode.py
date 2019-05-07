#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern) != len(str.split(' ')):
            return False
        w2p = {}
        p2w = {}
        for idx, w in enumerate(str.split(' ')):
            p = pattern[idx]
            if w not in w2p:
                w2p[w] = p
            elif w2p[w] != p:
                return False
            if p not in p2w:
                p2w[p] = w
            elif p2w[p] != w:
                return False
        return True
