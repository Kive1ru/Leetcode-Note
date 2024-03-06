class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            x = nums[i]
            if i > 0 and x == nums[i-1]:
                continue
            if x + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for j in range(i+1, n-2):
                y = nums[j]
                if j > i + 1 and y == nums[j-1]:
                    continue
                if x + y + nums[i+2] + nums[i+3] > target:
                    break
                if x + y + nums[-2] + nums[-1] < target:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    s = x + y + nums[left] + nums[right]
                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        res.append([x, y, nums[left], nums[right]])
                        left += 1
                        if left < right and nums[left] == nums[left-1]:
                            left += 1
                        right -= 1
                        while right > left and nums[right] == nums[right+1]:
                            right -= 1
        return res