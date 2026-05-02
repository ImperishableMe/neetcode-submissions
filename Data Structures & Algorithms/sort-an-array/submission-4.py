class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random
        def partition(nums, l, r):
            p_ind = random.randint(l, r)
            nums[r], nums[p_ind] = nums[p_ind], nums[r]
            pivot = nums[r]

            # [l, i) < pivot
            # i -> pivot
            i = l

            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        def quick_sort(nums, l, r):
            if l >= r:
                return
            
            p = partition(nums, l, r)
            quick_sort(nums, l, p - 1)
            quick_sort(nums, p + 1, r)

        quick_sort(nums, 0, len(nums) - 1)
        return nums