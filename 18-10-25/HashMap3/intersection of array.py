class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arrx = set(nums1)
        arry= set(nums2)
        res = list(arrx & arry)
        return res