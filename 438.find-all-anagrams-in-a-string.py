#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
class Solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     result = []
    #     target = collections.Counter(p)
    #     for start in range(len(s)-len(p)+1):
    #         if collections.Counter(s[start:start+len(p)]) == target:
    #             result.append(start)
    #     return result

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)-1])
        result = []
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] += 1 # include the current char
            if sCounter == pCounter:
                result.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return result
