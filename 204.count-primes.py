#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (28.33%)
# Total Accepted:    225.5K
# Total Submissions: 787.5K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
#


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        a = [True] * n
        a[0] = a[1] = False
        for i in range(2, n):
            if not a[i]:
                continue
            for j in range(2, (n-1)//i+1):
                a[i*j] = False
        return sum(a)
