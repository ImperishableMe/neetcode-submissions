import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(nums: list[int], st: int, en: int):
            # l, r = st, en
            p = random.randint(st, en - 1)
            nums[p], nums[en - 1] = nums[en - 1], nums[p]

            i, l = st, st
            while i < en - 1:
                if nums[i] < nums[en - 1]:
                    nums[i], nums[l] = nums[l], nums[i]
                    # nums[l] = nums[i]
                    l += 1
                    i += 1
                else:
                    i += 1
            nums[l], nums[en - 1] = nums[en - 1], nums[l]
            return l
            

        def quick_sort(nums: list[int], st: int, en: int):
            if en - st <= 1:
                return

            p = partition(nums, st, en)

            quick_sort(nums, st, p)
            quick_sort(nums, p + 1, en)

        # sorts nums[st: en]
        quick_sort(nums, 0, len(nums))
        return nums
        

