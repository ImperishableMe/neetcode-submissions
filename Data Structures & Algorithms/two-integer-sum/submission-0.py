class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last = {}
        for i, num in enumerate(nums):
            if target - num in last:
                return [last[target-num], i]
            last[num] = i
        assert False, "No result found"
        return []
