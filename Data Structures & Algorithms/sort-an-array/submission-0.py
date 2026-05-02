class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # buble sort
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums
        