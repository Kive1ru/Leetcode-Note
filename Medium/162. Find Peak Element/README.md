### 解法 
二分法

### 思路
题目要求寻找一串数组中的峰值，峰值是指比两边都大的数。这里可以用二分法来解决。因为题目说了数组中没有重复的数，所以可以用二分法。二分法的思路是找到中间的数，如果中间的数比两边都大，那么这个数就是峰值。如果中间的数比左边的数小，那么峰值一定在左边。如果中间的数比右边的数小，那么峰值一定在右边。所以可以用二分法来解决这个问题。

### 复杂度
Time Complexity: O(logn) 二分法的时间复杂度是O(logn)，所以是O(logn)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Binary Search

### Approach
The question requires finding the peak value in a string of arrays. The peak value refers to a number that is larger than both sides. This can be solved using the dichotomy method. Because the question says that there are no repeated numbers in the array, the binary search method can be used. The idea of ​​​​dichotomy is to find the middle number. If the middle number is larger than both sides, then this number is the peak. If the number in the middle is smaller than the number on the left, then the peak value must be on the left. If the number in the middle is smaller than the number on the right, then the peak must be on the right. So the binary search can be used to solve this problem.

### Complexity
Time Complexity: O(logn) The time complexity of binary search method is O(logn)  
Space Complexity: O(1) is all constant space, so it's O(1)