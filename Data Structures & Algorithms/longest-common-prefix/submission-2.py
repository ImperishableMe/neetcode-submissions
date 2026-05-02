class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        for i, ch in enumerate(strs[0]):
            pref += ch
            for j in range(1, len(strs)):
                if pref != strs[j][:len(pref)]:
                    return pref[:-1]
        return pref