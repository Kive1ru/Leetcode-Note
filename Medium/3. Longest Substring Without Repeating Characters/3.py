class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left = 0
        res = 0
        for right, x in enumerate(s):
            window[x] = window.get(x, 0) + 1
            while window[x] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left + 1)
        return res