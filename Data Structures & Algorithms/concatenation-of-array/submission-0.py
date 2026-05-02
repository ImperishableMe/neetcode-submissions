class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat = [0]* (2 * len(nums))
        for i in range(2 * len(nums)):
            if i >= len(nums):
                concat[i] = nums[i - len(nums)]
            else:
                concat[i] = nums[i]
        return concat

        