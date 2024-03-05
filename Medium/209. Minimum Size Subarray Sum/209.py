class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        left = 0
        total = 0
        for right, i in enumerate(nums):
            total += i
            while total >= target:
                res = min(res, (right - left + 1))
                total -= nums[left]
                left += 1
        return res if res <= n else 0