### 解法 
二分法

### 思路
题目要求寻找target所在的index。在一串单次递增或者二次递增的数组里。这个问题可以用二分法解决。is_blue是一个标志位，用来判断target在左边还是右边。思路和153题一样，跟数组的最后一个元素比较，如果mid比最后一个元素大，检查target是否大于最后一个元素，并且检查target是否小于mid，如果是，那么target在左边，否则在右边。如果mid比最后一个元素小，检查target是否大于最后一个元素，或者小于mid，如果是，那么target在左边，否则在右边。最后返回记录的位置即可。
### 复杂度
Time Complexity: O(logn) 二分法的时间复杂度是O(logn)，所以是O(logn)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Binary Search

### Approach
The question requires finding the index where the target is located. In a sequence of single-increasing or double-increasing arrays. This problem can be solved using the binary search method. is_blue is a flag used to determine whether the target is on the left or right. The idea is the same as question 153. Compare with the last element of the array. If mid is greater than the last element, check whether target is greater than the last element, and check whether target is less than mid. If so, then target is on the left, otherwise it is on the right. If mid is smaller than the last element, check whether target is larger than the last element, or smaller than mid. If so, then target is on the left, otherwise it is on the right. Finally, return to the recorded location.

### Complexity
Time Complexity: O(logn) The time complexity of binary search method is O(logn)  
Space Complexity: O(1) is all constant space, so it's O(1)