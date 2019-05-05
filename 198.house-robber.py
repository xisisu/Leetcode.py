#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (40.80%)
# Total Accepted:    300.9K
# Total Submissions: 736.5K
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
# Example 1:
#
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#


class Solution:
    # def __init__(self):
    #     self.cache = {}

    # def helper(self, nums: List[int], limit: int) -> int:
    #     if limit < 0:
    #         self.cache[limit] = 0
    #     if limit not in self.cache:
    #         self.cache[limit] = max(self.helper(nums, limit-2)+nums[limit], self.helper(nums, limit-1))
    #     return self.cache[limit]

    # def rob(self, nums: List[int]) -> int:
    #     return self.helper(nums, len(nums)-1)

    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     cache = []
    #     for v in nums:
    #         if len(cache) == 0:
    #             cache.append(v)
    #         elif len(cache) == 1:
    #             cache.append(max(v, cache[-1]))
    #         else:
    #             cache.append(max(v + cache[-2], cache[-1]))
    #     return cache[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prev1, prev2 = 0, 0
        for v in nums:
            prev1, prev2 = max(prev2+v, prev1), prev1
        return prev1
