class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Insertion sort
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j] # large elems move right
                j -= 1
            nums[j + 1] = key
        
        return nums