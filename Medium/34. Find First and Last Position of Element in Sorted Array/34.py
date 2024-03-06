class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        res = [-1, -1]

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res[0] = mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res[1] = mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return res
        '''
        left, right = 0, len(nums)
        res = [-1, -1]

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res[0] = mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res[1] = mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return res
        '''