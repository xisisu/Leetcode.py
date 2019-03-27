#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (42.28%)
# Total Accepted:    1.5M
# Total Submissions: 3.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# Example:
#
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
#
#


class Solution:
    def twoSum(self, nums, target):
        seen = dict()
        for idx, n in enumerate(nums):
            val = target - n
            if val in seen:
                return [seen[val], idx]
            seen[n] = idx
        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
