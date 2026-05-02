class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        r = n - 1
        for l in range(n-1, -1, -1):
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
        return r + 1