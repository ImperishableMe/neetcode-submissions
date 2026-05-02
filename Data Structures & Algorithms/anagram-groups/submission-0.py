class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] = anagrams.get(sorted_s, [])
            # .append(s)
            anagrams[sorted_s].append(s)
        return [val for val in anagrams.values()]