class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]:
                left = mid
            else:
                right = mid
        return right