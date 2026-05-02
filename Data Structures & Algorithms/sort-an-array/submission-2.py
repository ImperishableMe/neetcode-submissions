class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        def merge_sort(nums):
            n = len(nums)
            if n == 1:
                return nums
            mid = n // 2
            left_nums = merge_sort(nums[:mid])
            right_nums = merge_sort(nums[mid:])
            return merge(left_nums, right_nums)
        
        def merge(l1, l2):
            l = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    l.append(l1[i])
                    i += 1
                else:
                    l.append(l2[j])
                    j += 1
            while i < len(l1):
                l.append(l1[i])
                i += 1
            while j < len(l2):
                l.append(l2[j])
                j += 1
            return l
                
        return merge_sort(nums)

        