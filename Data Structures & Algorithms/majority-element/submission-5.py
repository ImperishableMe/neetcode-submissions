class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import random
        n = len(nums)
        while True:
            candidate = nums[random.randrange(n)]
            count = sum(1 for num in nums if num == candidate)
            if count * 2 > n:
                return candidate
        
        raise ValueError("majority where?")

