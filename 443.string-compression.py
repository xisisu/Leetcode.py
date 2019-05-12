#
# @lc app=leetcode id=443 lang=python3
#
# [443] String Compression
#
class Solution:
    def compress(self, chars: List[str]) -> int:
        start = 0
        idx = 0
        while idx < len(chars):
            total = 1
            while (idx+1) < len(chars) and chars[idx] == chars[idx+1]:
                idx += 1
                total += 1
            chars[start] = chars[idx]
            if total > 1:
                chars[start+1: start+1+len(str(total))] = str(total)
                start += len(str(total))
            start += 1
            idx += 1
        return start        

