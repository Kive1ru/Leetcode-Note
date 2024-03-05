### 解法 1
单调栈

### 思路 1
横向遍历，找到每个位置的左右边界，然后计算每个位置的容量，找到最大的容量。利用单调栈，对比当前位置和栈顶位置的高度，如果当前位置的高度大于栈顶位置的高度，那么就计算栈顶位置的容量，然后弹出栈顶位置，直到栈顶位置的高度大于等于当前位置的高度。然后将当前位置的索引入栈。这样可以找到每个位置的左右边界，然后计算每个位置的容量，找到最大的容量。

### 复杂度 1
Time Complexity: O(n) 遍历一次数组
Space Complexity: O(min(n,U)), 其中 U=max(height)-min(height)+1。注意栈中没有重复元素，在 height 值域很小的情况下，空间复杂度主要取决于 height 的值域范围。 

### Solution 1
Monotone stack

### Approach 1
Traverse horizontally, finding the left and right boundaries of each location, and then calculate the capacity of each location to find the maximum capacity. Using the monotonic stack, compare the height of the current position and the top position of the stack, if the height of the current position is greater than the height of the top position of the stack, then calculate the capacity of the top position of the stack, and then pop the top position of the stack until the height of the top position is greater than or equal to the height of the current position. The index of the current location is then pushed onto the stack. This allows you to find the left and right boundaries of each location, and then calculate the capacity of each location to find the maximum capacity.

### Complexity 1
Time Complexity: O(n) Traverse the array once
Space Complexity: O(min(n,U)), where U=max(height)-min(height)+1. Note that there are no duplicate elements in the stack, and in the case of a small height range, the space complexity is mainly determined by the height range.


### 解法 2
前后缀+双指针

### 思路 2
使用前后缀+双指针的思路。两个变量pre_max和suf_max分别记录当前位置的前缀最大值和后缀最大值。然后使用双指针的方法，一个指针指向数组的头部，一个指针指向数组的尾部，然后向中间移动。每次移动对比前后缀的大小，计算小侧的容量，然后移动小侧的指针。如果前缀的值大于后缀的值，那么移动后缀的指针，否则移动前缀的指针。这样可以找到每个位置的左右边界，然后计算每个位置的容量，找到最终的容量。

### 复杂度 2
Time Complexity: O(n) 一个while loop，两个指针向中间移动，所以是O(n)
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution 2
Presuffix + Two pointer

### Approach 2
Use prefix suffix + two pointer approach. Two variables, pre_max and suf_max, record the maximum prefix and maximum suffix values of the current location, respectively. A two-pointer approach is then used, with one pointer pointing to the head of the array and one pointer pointing to the tail of the array, then moving towards the middle. Each move compares the size of the prefix and suffix, calculates the capacity of the small side, and then moves the pointer of the small side. If the value of the prefix is greater than the value of the suffix, then the pointer of the suffix is moved, otherwise the pointer of the prefix is moved. This allows you to find the left and right boundaries of each location, and then calculate the capacity of each location to find the final capacity.

### Complexity 2
Time Complexity: O(n) A while loop, two Pointers moving toward the middle, so O(n)
Space Complexity: O(1) is all constant space, so it's O(1)