#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#


class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    #     r = num
    #     while r * r > num:
    #         r = (r + num/r) // 2
    #     return r*r == num

    def isPerfectSquare(self, num: int) -> bool:
        l, h = 1, num
        while l <= h:
            mid = (l+h) // 2
            cur = mid * mid
            if cur < num:
                l = mid + 1
            elif cur > num:
                h = mid - 1
            else:
                return True
        return False
