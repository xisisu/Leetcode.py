#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     result = []
    #     for n in nums1:
    #         if n in nums2:
    #             result.append(n)
    #             nums2.remove(n)
    #     return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a&b).elements())

