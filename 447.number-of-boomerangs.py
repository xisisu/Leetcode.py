#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for p in points:
            cur_map = {}
            for q in points:
                d = (p[0]-q[0])**2 + (p[1]-q[1])**2
                cur_map[d] = cur_map.get(d, 0) + 1
            for v in cur_map.values():
                result += v * (v-1)
        return result
