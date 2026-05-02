class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import random
        while True:
            value = random.choice(nums)
            if nums.count(value) * 2 > len(nums):
                return value