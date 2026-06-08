class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[0]:
                hi = mid
            else:
                lo = mid + 1
        return nums[0] if lo == len(nums) else nums[lo] 