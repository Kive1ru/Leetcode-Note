class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = inf
        for i in range(n-2):
            x = nums[i]
            if i and x == nums[i - 1]:
                continue
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三个数的和不会比 s 还小
                if s - target < min_diff:
                    ans = s  # 由于下一行直接 break，这里无需更新 min_diff
                    break
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < min_diff:
                    min_diff = target - s
                    ans = s
                    continue

            left = i + 1
            right = n - 1
            while left < right:
                s = x + nums[left] + nums[right]
                if s == target:
                    return target
                if s > target:
                    if s - target < min_diff:
                        min_diff = s - target
                        ans = s
                    right -= 1
                elif s < target:
                    if target - s < min_diff:  # s 与 target 更近
                        min_diff = target - s
                        ans = s
                    left += 1
        return ans
