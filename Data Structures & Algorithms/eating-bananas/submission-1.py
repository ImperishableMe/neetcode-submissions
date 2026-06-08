class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def required_time(k: int) -> int:
            return sum(
                (pile + k - 1) // k for pile in piles
            )
        
        lo, hi = 1, max(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            if required_time(mid) <= h: # not enough time
                hi = mid
            else:
                lo = mid + 1
        
        return lo
        
