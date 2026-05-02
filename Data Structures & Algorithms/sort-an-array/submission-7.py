class Solution:

    # [st, en)
    def merge_sort(self, nums: List[int], st: int, en: int):
        if en - st <= 1:
            return
        mid = (st + en) // 2
        self.merge_sort(nums, st, mid)
        self.merge_sort(nums, mid, en)
        merge = []
        i, j = st, mid
        while i < mid and j < en:
            if nums[i] < nums[j]:
                merge.append(nums[i])
                i += 1
            else:
                merge.append(nums[j])
                j += 1

        while i < mid:
            merge.append(nums[i])
            i += 1 
        while j < en:
            merge.append(nums[j])
            j += 1
            
        nums[st: en] = merge

    def sortArray(self, nums: List[int]) -> List[int]:
        # merge sort
        n = len(nums)
        self.merge_sort(nums, 0, n)
        return nums

    