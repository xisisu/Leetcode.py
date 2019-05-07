#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) <= 2:
            return max(nums)
        return sorted(set(nums))[-3]

