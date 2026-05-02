class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def mask(s: str) -> dict[str, int]:
            cnt = defaultdict(int)
            for ch in s:
                cnt[ch] += 1
            return cnt
        
        return mask(s) == mask(t)