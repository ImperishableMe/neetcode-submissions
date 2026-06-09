class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s1, s2 = t, s

        charSet = set(t)
        # print(charSet)

        n1, n2 = len(s1), len(s2)
        count_1, count_2 = defaultdict(int), defaultdict(int)
        
        for ch in s1:
            count_1[ch] += 1
        
        def add(r):
            count_2[s2[r]] += 1
        
        def remove(r):
            count_2[s2[r]] -= 1
        
        l = 0
        ans = ""
        start, length = 0, float('inf')

        for r in range(n2):
            add(r)
            # print(s2[r], count_2, count_1)
            while (
                l <= r and 
                all(count_2[k] >= count_1[k] for k in charSet)
                #any(count_2[k] > count_1[k] for k in charSet)
            ):
                if r - l + 1 < length:
                    start, length = l, r - l + 1

                remove(l)
                l += 1
        ans = "" if length == float('inf') else s2[start: start + length]
        return ans
            
