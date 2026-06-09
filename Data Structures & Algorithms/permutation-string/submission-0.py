class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        count_1, count_2 = defaultdict(int), defaultdict(int)
        
        for ch in s1:
            count_1[ch] += 1
        
        for r in range(n2):
            count_2[s2[r]] += 1
            print(r, count_2)
            if r >= n1:
                count_2[s2[r - n1]] -= 1
                if count_2[s2[r - n1]] == 0:
                    del count_2[s2[r - n1]]
                
            if count_1 == count_2:
                return True
        
        return False
            
