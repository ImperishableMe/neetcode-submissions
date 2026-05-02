class Solution:

    def encode(self, strs: List[str]) -> str:
        codes = [str(len(s)) + '#' + s for s in strs]
        return ''.join(codes)

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            size = int(s[i : j])
            words.append(s[j + 1: j + size + 1])
            i = j + size + 1
        return words        


