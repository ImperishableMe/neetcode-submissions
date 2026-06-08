from bisect import bisect_right

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        is_even = total % 2 == 0
        
        def find_k_th_elem(k: int):
            """
            k is 1 based
            """
            lo, hi = -10**7, 10**7
            if k > n1 + n2:
                raise ValueError(f"{k} is too big")
            
            while lo < hi:
                mid = (lo + hi) // 2
                smaller_eq = bisect_right(nums1, mid)
                smaller_eq += bisect_right(nums2, mid)
                # print(mid, smaller, k)
                if smaller_eq <= k - 1:
                    lo = mid + 1
                else:
                    hi = mid
            
            return lo
        
        if is_even:
            return (
                find_k_th_elem(total / 2) + 
                find_k_th_elem(total / 2 + 1)
            ) / 2
        return find_k_th_elem((total + 1) // 2)
