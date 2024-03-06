class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        left = 0
        p = 1
        for right, x in enumerate(nums):
            p *= x
            while p >= k:
                p /= nums[left]
                left += 1
            res += right - left + 1
        return res
