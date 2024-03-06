class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        '''
        # brute force
        ans = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans
        '''
        # two pointer
        nums.sort()
        left, right = 0, len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1
        return ans