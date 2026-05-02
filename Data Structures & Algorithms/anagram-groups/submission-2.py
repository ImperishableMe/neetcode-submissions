class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def code(s: str)-> tuple[int]:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - ord('a')] += 1
            return tuple(cnt)

        anagrams = defaultdict(list)
        for s in strs:
            coded_s = code(s)
            # anagrams[coded_s] = anagrams.get(coded_s, [])
            anagrams[coded_s].append(s)
        return [val for val in anagrams.values()]