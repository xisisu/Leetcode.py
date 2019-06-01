#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (54.89%)
# Likes:    363
# Dislikes: 310
# Total Accepted:    137.4K
# Total Submissions: 249.7K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#
class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     res, cur = 0, 0
    #     for n in nums:
    #         if n == 0:
    #             res = max(res, cur)
    #             cur = 0
    #         else:
    #             cur += 1
    #     return max(res, cur)
        
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums_str = ''.join(map(str, nums))
        nums_list = nums_str.split('0')
        return len(max(nums_list))
