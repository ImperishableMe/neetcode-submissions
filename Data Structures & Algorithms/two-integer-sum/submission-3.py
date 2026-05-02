class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nl = [(num, i) for i, num in enumerate(nums)]
        nl.sort(key= lambda x: x[0])
        l, r = 0, n-1

        while l < r:
            cur = nl[l][0] + nl[r][0]
            if cur < target:
                l += 1
            elif cur > target:
                r -= 1
            else:
                return sorted([nl[l][1], nl[r][1]])
        assert False, "No result found"
        return []
