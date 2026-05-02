import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:       
        n = len(nums)
        while True:
            candidate = random.choice(nums)
            count = nums.count(candidate)
            if count * 2 > n:
                return candidate
        
        raise ValueError("majority where?")

