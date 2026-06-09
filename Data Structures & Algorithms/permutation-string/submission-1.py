class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        count_1, count_2 = defaultdict(int), defaultdict(int)
        
        for ch in s1:
            count_1[ch] += 1

        matched = 0
        for ch in range(ord('a'), ord('z') + 1):
            matched += 1 if count_1[chr(ch)] == 0 else 0
        
        def add(r):
            nonlocal matched
            matched -= 1 if count_2[s2[r]] == count_1[s2[r]] else 0
            count_2[s2[r]] += 1
            matched += 1 if count_2[s2[r]] == count_1[s2[r]] else 0
        
        def remove(r):
            nonlocal matched
            matched -= 1 if count_2[s2[r]] == count_1[s2[r]] else 0
            count_2[s2[r]] -= 1
            matched += 1 if count_2[s2[r]] == count_1[s2[r]] else 0

        for r in range(n2):
            add(r)

            print(r, count_2)
            if r >= n1:
                remove(r - n1) 
            if matched == 26:
                return True
        
        return False
            
