class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_seen = defaultdict(int)
        for i, num in enumerate(nums):
            need = target - num
            if need in last_seen:
                return [last_seen[need], i]
            else: 
                last_seen[num] = i
        return []