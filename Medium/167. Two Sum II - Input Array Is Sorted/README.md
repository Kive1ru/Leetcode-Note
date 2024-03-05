### 解法 
双指针

### 思路
因为是有序数组，所以可以使用双指针的方法，一个指针指向数组的头，一个指针指向数组的尾，然后向中间移动，直到找到答案。如果两个指针指向的元素的和大于目标值，那么尾指针向前移动，如果两个指针指向的元素的和小于目标值，那么头指针向后移动。（因为两端之和如果小于目标，说明numbers[left]太小了。两端之和如果大于目标，说明numbers[right]太大了。）

### 复杂度
Time Complexity: O(n) 一个while loop，两个指针向中间移动，所以是O(n)
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
Because it is an ordered array, you can use the double pointer method. One pointer points to the head of the array, and the other points to the tail of the array, and then moves toward the middle until the answer is found. If the sum of the elements pointed to by the two pointers is greater than the target value, then the tail pointer moves forward. If the sum of the elements pointed to by the two pointers is less than the target value, then the head pointer moves backward. (Because if the sum of the two ends is less than the target, it means that numbers[left] is too small. If the sum of the two ends is greater than the target, it means that numbers[right] is too big.)

### the complexity
Time Complexity: O(n) A while loop, the two pointers move to the middle, so it is O(n)
Space Complexity: O(1) It’s all constant space, so it’s O(1)