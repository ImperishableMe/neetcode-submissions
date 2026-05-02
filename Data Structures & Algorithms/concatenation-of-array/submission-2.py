class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [ 
            nums[i] if i < n else nums[i - n]
            for i in range(2*n)
        ]
        # return 