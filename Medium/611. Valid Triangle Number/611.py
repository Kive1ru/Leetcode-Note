class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for k in range(2, len(nums)):
            c = nums[k]
            i = 0  # a=nums[i]
            j = k - 1  # b=nums[j]
            while i < j:
                if nums[i] + nums[j] > c:
                    # 由于 nums 已经从小到大排序
                    # nums[i]+nums[j] > c 同时意味着：
                    # nums[i+1]+nums[j] > c
                    # nums[i+2]+nums[j] > c
                    # ...
                    # nums[j-1]+nums[j] > c
                    # 从 i 到 j-1 一共 j-i 个
                    ans += j - i
                    j -= 1
                else:
                    # 由于 nums 已经从小到大排序
                    # nums[i]+nums[j] <= c 同时意味着
                    # nums[i]+nums[j-1] <= c
                    # ...
                    # nums[i]+nums[i+1] <= c
                    # 所以在后续的循环中，nums[i] 不可能作为三角形的边长，没有用了
                    i += 1
        return ans