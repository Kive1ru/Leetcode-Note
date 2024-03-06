### 解法 
双指针

### 思路
可以先排序，然后使用双指针的方法。一个指针指向数组头，一个指针指向数组尾，然后向中间移动直到找到答案。如果两个指针指向的元素之和大于目标值，那么尾指针向前移动。如果两个指针指向的元素之和小于目标值，顺便更新ans。ans = right - left，因为数组已经排序过，所有left右侧的数值加上left都会小于targett，头指针向后移动。

### 复杂度
Time Complexity: O(n) 一个while loop，两个指针向中间移动，所以是O(n)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
You can sort first and then use the two pointer method. A pointer points to the head of the array, a pointer points to the end of the array, and then moves toward the middle until the answer is found. If the sum of the elements pointed to by the two pointers is greater than the target value, then the tail pointer moves forward. If the sum of the elements pointed to by the two pointers is less than the target value, ans is updated by the way. ans = right - left, because the array has been sorted, all values ​​on the right side of left plus left will be less than targett, and the head pointer moves backward.

### the complexity
Time Complexity: O(n) A while loop, the two pointers move to the middle, so it is O(n)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)