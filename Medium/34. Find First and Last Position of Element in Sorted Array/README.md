### 解法 
二分法

### 思路
题目要求寻找target的起始和终止位置，所以可以用二分法左闭右闭left<=right,如果target等于mid,则记录mid的位置在list[0]，如果target小于mid,则在左边找right-1，如果target大于mid,则在右边找 left+1。重置right，再次用相同的处理方法得到list[1],最后返回记录的位置。

### 复杂度
Time Complexity: O(logn) 二分法的时间复杂度是O(logn)，所以是O(logn)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Binary Search

### Approach
They want to find the start and end positions of target, so you can use a dichotomy to close left and right. left<=right, if target is equal to mid, then record the position of mid in list[0], if target is less than mid, then find right-1 on the left. If target is greater than mid, look for left+1 on the right. Reset right, use the same process again to get list[1], and finally return the record location.

### Complexity
Time Complexity: O(logn) The time complexity of binary search method is O(logn)  
Space Complexity: O(1) is all constant space, so it's O(1)