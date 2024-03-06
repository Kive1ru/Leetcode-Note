class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = -1, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]