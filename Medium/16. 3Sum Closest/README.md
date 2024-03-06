### 解法 
双指针

### 思路
可以变为有序数组，参考 Medium 15 3Sum，此题为变种，用min_diff去记录最小差值。可以使用双指针的方法。此题要求三数之和离target差距最小，且不重复。nums[i] + nums[j] + nums[k] 约等于 target 可以变为 nums[j] + nums[k] = -nums[i]。所以可以固定一个数，然后使用双指针的方法找到另外两个数。这里需要注意的是，找到一个解后，可以选择跳过重复的解去优化。一个指针指向i+1，一个指针指向数组的尾，然后向中间移动，直到找到答案。如果两个指针指向的元素的和大于target，更新当前最小差距，那么尾指针向前移动，如果两个指针指向的元素的和小于target，更新当前最小差距，那么头指针向后移动。如果等于target，直接返回和（因为两端之和如果小于目标，说明numbers[left]太小了。两端之和如果大于目标，说明numbers[right]太大了。）优化步骤在于，如果nums[i] + nums[i+1] + nums[i+2] > target，说明后面的数都大于target，不可能是最近的和，直接break，返回前三个数的和。如果nums[i] + nums[n-2] + nums[n-1] < 0，说明前面的数都小于target，不可能是最近的和，更新当前最小差距。

### 复杂度
Time Complexity: O(n^2) sort本身是O(nlogn)，一个for loop，一个while loop，两个指针向中间移动，所以是O(n^2)。 O(n^2) > O(nlogn) 所以是O(n^2)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
It can be turned into an ordered array, refer to Medium 15 3Sum, this title is a variant, use min_diff to record the minimum difference. You can use the double pointer method. This question requires that the sum of three numbers is the smallest distance from the target and does not repeat. nums[i] + nums[j] + nums[k] is approximately equal to target and can be changed to nums[j] + nums[k] = -nums[i]. So you can fix one number and then use the double pointer method to find the other two numbers. What needs to be noted here is that after finding a solution, you can choose to skip repeated solutions for optimization. A pointer points to i+1, a pointer points to the end of the array, and then moves toward the middle until the answer is found. If the sum of the elements pointed to by the two pointers is greater than target, the current minimum gap is updated, and the tail pointer moves forward. If the sum of the elements pointed by the two pointers is less than target, the current minimum gap is updated, and the head pointer moves backward. If it is equal to target, the sum is returned directly (because if the sum of the two ends is less than the target, it means that numbers [left] is too small. If the sum of the two ends is greater than the target, it means that numbers [right] is too large.) The optimization step is that if nums [i] + nums[i+1] + nums[i+2] > target, indicating that the following numbers are greater than target and cannot be the nearest sum. Update the current minimum gap and break directly. If nums[i] + nums[n-2] + nums[n-1] < 0, it means that the previous numbers are smaller than the target and cannot be the latest sum. Update the current minimum gap.

### the complexity
Time Complexity: O(n^2) sort itself is O(nlogn), a for loop, a while loop, and two pointers move to the middle, so it is O(n^2). O(n^2) > O(nlogn) so O(n^2)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)