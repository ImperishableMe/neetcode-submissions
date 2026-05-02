class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def char_cnt(s: str) -> list[int]:
            cnt = {}
            for ch in s:
                cnt[ord(ch)] = cnt.get(ord(ch), 0) + 1
            return cnt
        
        # return sorted(s) == sorted(t)
        return char_cnt(s) == char_cnt(t)
    
    