class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_len = 0
        l = 0
        max_f = 0

        for r in range(len(s)):
            count[s[r]] += 1
            if count[s[r]] > max_f:
                max_f = count[s[r]]
            
            while r - l + 1 - max_f > k:
                count[s[l]] -= 1
                max_f = max(count.values())
                l += 1

            max_len = max(max_len, r - l + 1)
        return max_len
