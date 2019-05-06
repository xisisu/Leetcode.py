#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l <= h:
            mid = (l+h) // 2
            cur = guess(mid)
            if cur == -1:
                h = mid - 1
            elif cur == 1:
                l = mid + 1
            else:
                return mid
        return None        

