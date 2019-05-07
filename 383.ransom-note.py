#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     c1, c2 = map(collections.Counter, (ransomNote, magazine))
    #     return all(c2[k]>=c1[k] for k in c1)

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in string.ascii_lowercase)
