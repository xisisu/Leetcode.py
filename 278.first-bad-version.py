#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l < h:
            mid = (l+h) // 2
            if isBadVersion(mid):
                h = mid
            else:
                l = mid+1
        return l
