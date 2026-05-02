class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num] += 1
            if count[num] * 2 > n:
                return num
        raise ValueError("majority where?")
