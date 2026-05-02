class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                value = num
            cnt = cnt + 1 if value == num else cnt - 1

        return value