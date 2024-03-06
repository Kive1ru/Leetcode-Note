### 解法 
快慢指针

### 思路
题目要求将linked list重新排序，从中间node开始，将后半部分倒序插入到前半部分中。可以使用快慢指针的方法找到中间node，然后将后半部分倒序，最后将两部分合并即可。做法可以先参考876 middle of the linked list，找到中间node，然后参考206 reverse linked list，将后半部分倒序，最后将两部分合并即可。

### 复杂度
Time Complexity: O(n) 因为只有一个循环，所以时间复杂度是O(n)  
Space Complexity: O(1) 全是常数空间，所以是O(1)


### Solution
Slow and fast pointers

### Approach
The question requires reordering the linked list, starting from the middle node, and inserting the second half into the first half in reverse order. You can use the fast and slow pointer method to find the middle node, then reverse the second half, and finally merge the two parts. To do this, you can first refer to 876 middle of the linked list to find the middle node, then refer to 206 reverse linked list, reverse the second half, and finally merge the two parts.

### the complexity
Time Complexity: O(n) Because there is only one loop, the time complexity is O(n)    
Space Complexity: O(1) It’s all constant space, so it’s O(1)