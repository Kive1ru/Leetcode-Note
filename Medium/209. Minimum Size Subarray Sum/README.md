### 解法 
滑动窗口

### 思路
题目要求寻找最短满足target的子数组的长度，所以可以使用滑动窗口的方法。定义两个指针，分别指向滑动窗口的左右边界，然后移动右边界，直到找到满足条件的子数组，然后移动左边界，直到找到最短的子数组。如果滑动窗口的和小于target，那么右边界向右移动，如果滑动窗口的和大于target，那么左边界向右移动。

### 复杂度
Time Complexity: O(n) 两个指针向右移动，所以是O(n)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Sliding window

### Approach
They want to find the shortest length of the subarray that meets the target, so we can use the sliding window method. Define two Pointers that point to the left and right boundaries of the sliding window, then move the right boundary until it finds a subarray that satisfies the condition, then move the left boundary until it finds the shortest subarray. If the sum of the sliding window is less than target, then the right boundary moves to the right, and if the sum of the sliding window is greater than target, then the left boundary moves to the right.

### Complexity
Time Complexity: O(n) The two Pointers move to the right, so it's O(n)  
Space Complexity: O(1) is all constant space, so it's O(1)