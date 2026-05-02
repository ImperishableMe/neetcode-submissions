class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs[0]) == 0:
            return ""
        for l in range(0, len(strs[0])):
            cur_ch = strs[0][l]
            for s in strs:
                if l >=  len(s) or s[l] != cur_ch:
                    return s[:l]
        return strs[0]