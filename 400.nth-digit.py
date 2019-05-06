#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        len, count = 1, 9
        while n > len*count:
            n -= len*count
            len+=1
            count *= 10
        real_num = (n-1) // len + 10**(len-1)
        idx = (n-1) % len
        return (real_num // 10**(len-idx-1)) % 10

