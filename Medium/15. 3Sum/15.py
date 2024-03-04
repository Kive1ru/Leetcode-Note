class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] > 0:
                break
            if x + nums[-2] + nums[-1] < 0:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                s = x + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    res.append([x, nums[left], nums[right]])
                    left += 1
                    if left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
        return res