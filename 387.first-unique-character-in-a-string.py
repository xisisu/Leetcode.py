#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     d = collections.Counter(s)
    #     for idx, c in enumerate(s):
    #         if d[c] == 1:
    #             return idx
    #     return -1

    def firstUniqChar(self, s: str) -> int:
        return min([s.find(c) for c in string.ascii_lowercase if s.count(c) == 1] or [-1])
