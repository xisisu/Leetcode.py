#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
class Solution:
    def reverseVowels(self, s: str) -> str:
        l, h = 0, len(s)-1
        vowel = set(list("aeiouAEIOU"))
        res = list(s)
        while l < h:
            if s[l] not in vowel:
                l += 1
            elif s[h] not in vowel:
                h -= 1
            else:
                res[l], res[h] = s[h], s[l]
                l+=1
                h-=1
        return ''.join(res)

