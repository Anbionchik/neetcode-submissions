class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l, t_l = list(s), list(t)
        return sorted(s_l) == sorted(t_l)