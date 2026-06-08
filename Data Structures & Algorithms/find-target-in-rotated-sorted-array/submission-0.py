from bisect import bisect_right

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[0]:
                hi = mid
            else:
                lo = mid + 1
        
        pivot = lo if lo < len(nums) else 0

        print(f"pivot: {pivot}")

        def find_index(l: int, r: int) -> int:
            upper_bound = bisect_right(nums, target, lo=l, hi=r)
            return (upper_bound - 1
                if upper_bound != l and nums[upper_bound - 1] == target 
                else -1
            )
        
        if nums[pivot] <= target <= nums[-1]:
            return find_index(pivot, len(nums))
        
        return find_index(0, pivot)