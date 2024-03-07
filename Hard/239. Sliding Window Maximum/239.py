class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        queue = collections.deque()
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        res = [queue[0]]
        for j in range(k, len(nums)):
            if queue[0] == nums[j-k]:
                queue.popleft()
            while queue and queue[-1] < nums[j]:
                queue.pop()
            queue.append(nums[j])
            res.append(queue[0])
        return res