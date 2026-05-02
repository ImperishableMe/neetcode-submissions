class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def merge_sort(nums, l, r):
            if l == r:
                return
            m = (l + r) >> 1
            merge_sort(nums, l, m)
            merge_sort(nums, m + 1, r)
            merge(nums, l, m, r)

        def merge(nums, l, m, r):
            left = nums[l: m + 1]
            right = nums[m + 1: r + 1]
            L, R = 0, 0

            while L < len(left) and R < len(right):
                if left[L] < right[R]:
                    nums[l] = left[L]
                    L += 1
                else:
                    nums[l] = right[R]
                    R += 1
                l += 1
            
            while L < len(left):
                nums[l] = left[L]
                l += 1
                L += 1
            while R < len(right):
                nums[l] = right[R]
                l += 1
                R += 1
    
        merge_sort(nums, 0, len(nums))
        return nums

        