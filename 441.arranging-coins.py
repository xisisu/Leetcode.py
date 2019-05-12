#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8*n+1)-1)//2)

