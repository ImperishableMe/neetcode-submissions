class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        next_pos = 0

        for i in range(n):
            if nums[i] == val:
                continue
            nums[next_pos] = nums[i]
            next_pos += 1
        
        return next_pos