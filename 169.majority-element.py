#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (51.62%)
# Total Accepted:    360.4K
# Total Submissions: 694.7K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always
# exist in the array.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: 3
#
# Example 2:
#
#
# Input: [2,2,1,1,1,2,2]
# Output: 2
#
#
#


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     return sorted(nums)[len(nums)//2]

    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for v in nums:
            if count == 0:
                res = v
            if res == v:
                count += 1
            else:
                count -= 1
        return res
