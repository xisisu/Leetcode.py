#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a, b = map(collections.Counter, (s, t))
        return (b-a).popitem()[0]

    # def findTheDifference(self, s: str, t: str) -> str:
    #     res = 0
    #     for c in s+t:
    #         res ^= ord(c)
    #     return chr(res)
