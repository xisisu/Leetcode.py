#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a, b = map(collections.Counter, (s, t))
        return (b-a).elements()        

