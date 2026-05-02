class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, ch in enumerate(strs[0]):
            if any(len(s) <= i or s[i] != ch for s in strs):
                return strs[0][:i]
        return strs[0]