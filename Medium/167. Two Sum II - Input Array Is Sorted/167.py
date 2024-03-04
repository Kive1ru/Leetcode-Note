class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if target == total:
                return [left+1, right+1]
            if target > total:
                left += 1
            else:
                right -= 1
        return [-1, -1]