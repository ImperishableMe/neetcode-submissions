import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:       
        major = -1
        count = 0
        for num in nums:
            if count == 0:
                major = num
            
            if major == num:
                count += 1
            else:
                count -= 1
        
        return major
            
        raise ValueError("majority where?")

