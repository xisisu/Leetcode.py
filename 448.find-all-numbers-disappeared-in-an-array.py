#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     return list(set(range(1, len(nums)+1)) - set(nums))

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            cur = abs(n)
            nums[cur-1] = -1 * abs(nums[cur-1])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
