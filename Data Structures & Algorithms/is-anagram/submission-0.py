class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def char_cnt(s: str) -> list[int]:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            return cnt
        
        # return sorted(s) == sorted(t)
        return char_cnt(s) == char_cnt(t)
    
    