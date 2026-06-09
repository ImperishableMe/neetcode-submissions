from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {} # (char to index)
        left_point = 0
        ans = 0
        for i, ch in enumerate(s):
            # print(ch)
            if ch in last:
                left_point = max(left_point, last[ch] + 1)
            last[ch] = i
            ans = max(ans, i - left_point + 1)
        
        return ans