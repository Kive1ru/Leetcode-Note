### 解法 
双指针

### 思路
可以先排序，去遍历第三个边，然后用双指针去找第一个和第二个边。k从index 2开始遍历，然后用双指针去找第一个和第二个边。第二个边为k-1，第一个边为0。判断是否找到了，可以根据前两个边之和是否大于第三边。如果大于，因为有序数组，所以第一个边到第二个边之间的边都可以和第三个边组成三角形。所以ans += right - left。然后right向前移动。如果小于，因为有序数组，第一个边到第二个边之间的边都不可以和第三个边组成三角形，left向后移动。

### 复杂度
Time Complexity: O(n^2) for loop + while loop  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
You can sort first, traverse the third edge, and then use two pointers to find the first and second edges. k starts traversing from index 2, and then uses double pointers to find the first and second edges. The second edge is k-1 and the first edge is 0. To determine whether it is found, you can judge whether the sum of the first two sides is greater than the third side. If it is greater than, because it is an ordered array, the sides between the first side and the second side can form a triangle with the third side. So ans += right - left. Then right moves forward. If it is less than, because of the ordered array, the sides between the first side and the second side cannot form a triangle with the third side, and left moves backward.

### the complexity
Time Complexity: O(n^2) for loop + while loop  
Space Complexity: O(1) It’s all constant space, so it’s O(1)