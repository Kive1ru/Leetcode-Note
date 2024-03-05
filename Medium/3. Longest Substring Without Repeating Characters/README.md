### 解法 
滑动窗口

### 思路
The problem asks to find the longest non-repeating string, you can use the sliding window method + dictionary to find. Define two Pointers to the left and right edges of the sliding window, then move the right edge to add characters to the dictionary, check if there are more than 1 characters in the dictionary, then move the left edge to exclude characters until all characters are 1. Update the maximum length. Finally, the maximum length is returned.

### 复杂度
Time Complexity: O(n) 两个指针向右移动，所以是O(n)  
Space Complexity: O(1) 因为题目限定了s只包含英文字母、数字、符号和空格，所以是O(128)或者O(len(set(s)))，所以是O(1)


### Solution
Sliding window

### Approach
The problem is to find the number of subarrays whose product is less than k, so you can use the sliding window method. Define two Pointers that point to the left and right boundaries of the sliding window, then move the right boundary until it finds a subarray that satisfies the condition, then move the left boundary until it finds a subarray that satisfies the condition. If the product of the sliding window is less than k, then the right boundary moves to the right, and if the product of the sliding window is greater than k, then the left boundary moves to the right. (See Medium-209)

### Complexity
Time Complexity: O(n) The two Pointers move to the right, so it's O(n)  
Space Complexity: O(1) Because the complexity of s is limited to letters, numbers, symbols and Spaces, it is O(128) or O(len(set(s)), so it is O(1)