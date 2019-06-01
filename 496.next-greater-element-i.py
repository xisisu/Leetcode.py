#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (59.32%)
# Likes:    788
# Dislikes: 1282
# Total Accepted:    96.2K
# Total Submissions: 161.6K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2. 
# 
# 
# 
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
# 
# 
# Example 1:
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
# ⁠   For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
# ⁠   For number 1 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# Example 2:
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
# ⁠   For number 2 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# 
# Note:
# 
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
# 
# 
#
class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     reverse = dict()
    #     for k, v in enumerate(nums2):
    #         reverse[v] = k
    #     result = []
    #     for n in nums1:
    #         idx = reverse.get(n)+1
    #         while idx < len(nums2) and nums2[idx] < n:
    #             idx += 1
    #         if idx == len(nums2):
    #             result.append(-1)
    #         else:
    #             result.append(nums2[idx])
    #     return result

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, map = [], dict()
        for n in nums2:
            while len(stack) > 0 and stack[-1] < n:
                map[stack[-1]] = n
                stack.pop(-1)
            stack.append(n)
        return [map.get(n, -1) for n in nums1]

    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     return [next((y for y in nums2[nums2.index(x):] if y > x), -1) for x in nums1]
    

