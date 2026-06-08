class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return -1 if l == 0 or nums[l - 1] != target else l - 1