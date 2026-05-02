class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # (key, List[word])
        for str in strs:
            groups["".join(sorted(str))].append(str)
        return list(groups.values())