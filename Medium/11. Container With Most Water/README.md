### 解法 
双指针

### 思路
因为是要找到最大的容器面积，所以我们可以从两边开始，然后向中间移动。每次移动的时候，我们都要计算当前的容器的容量，然后和之前的最大容量比较，如果大于之前的最大容量，就更新最大容量。然后我们移动两个指针中较短的高度的，因为如果移动较长的那个，容器的容量肯定会减小。所以我们每次都移动较短的那个指针，直到两个指针相遇。

### 复杂度
Time Complexity: O(n) 一个while loop，两个指针向中间移动，所以是O(n)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Two pointer

### Approach
Because we want to find the largest container area, we can start from both sides and move toward the middle. Every time we move, we have to calculate the capacity of the current container, and then compare it with the previous maximum capacity. If it is greater than the previous maximum capacity, update the maximum capacity. Then we move the height of the shorter of the two pointers, because if we move the longer one, the capacity of the container will definitely decrease. So we move the shorter pointer each time until the two pointers meet.

### Complexity
Time Complexity: O(n) A while loop, the two pointers move to the middle, so it is O(n)  
Space Complexity: O(1) It’s all constant space, so it’s O(1)