class Solution:
    def trap(self, height: List[int]) -> int:
        # mono stack
        st = []
        ans = 0
        for i, h in enumerate(height):
            while st and h > height[st[-1]]:
                bot = height[st.pop()]
                if not st:
                    break
                left = st[-1]
                dh = min(height[left], h) - bot
                ans += (i - left - 1) * dh
            st.append(i)
        return ans