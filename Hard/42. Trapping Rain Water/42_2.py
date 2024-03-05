class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer
        pre_max = 0
        suf_max = 0
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
